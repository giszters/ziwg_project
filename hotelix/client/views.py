# -*- coding: utf-8 -*-
from collections import OrderedDict
import datetime
from datetime import timedelta

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, \
    TemplateView

from client.forms import OrderForm, OrderCreateForm, ClientForm
from client.models import Client, Order
from hotelix.views import SuccessMixin
from structure.models import House, Floor, Room


class ClientList(ListView):
    model = Client


class ClientEdit(SuccessMixin, UpdateView):
    model = Client
    template_name = 'edit.html'
    form_class = ClientForm


class ClientCreate(CreateView):
    model = Client
    template_name = 'create.html'
    form_class = ClientForm
    success_url = reverse_lazy('client:client_list')


class ClientDelete(DeleteView):
    model = Client
    success_url = discard_url = reverse_lazy('client:client_list')
    template_name = 'delete.html'
    info = u"Uwaga - wszystkie rezerwacje i zamówienia tego klienta zostaną usunięte"


class OrderList(TemplateView):
    template_name = 'client/order_list.html'

    def get_context_data(self, **kwargs):
        context = super(OrderList, self).get_context_data(**kwargs)
        # switch between houses
        house_id = self.request.GET.get('house_id')
        start_date = self.request.GET.get('start_date', '')
        all_houses = House.objects.order_by('id')
        house = House.objects.get(pk=house_id) if house_id else all_houses[0]
        floors = Floor.objects.filter(house=house)
        print "start_date",start_date

        if len(start_date) > 0:
            d1 = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            d2 = d1 + timedelta(13)
        else: # default datetimes
            d1 = datetime.date(2014, 11, 3)
            d2 = datetime.date(2014, 11, 16)
        date_range = (d2 - d1).days + 1
        orders = OrderedDict()
        for floor in floors:
            floor.rooms = floor.room_set.order_by('id')
            orders[floor.number] = OrderedDict()
            for room in floor.rooms.all():
                room_description = []
                for n in xrange(date_range):
                    room_description.append(room.is_reserved(d1 + timedelta(n)))
                """ NIE USUWAĆ - proof of concept na zrobienie colspanów rezerwacji
                distinct_orders = set(map(lambda x: x['order_id'], room_description))
                distinct_orders = filter(lambda x: x > 0, distinct_orders)
                for order_id in distinct_orders:
                    order = filter(lambda x: x['order_id']==order_id, room_description)[0]
                    colspan = reduce(lambda x,y: x + int(y['order_id']==order_id), room_description, 0)
                    # i tu nie zadziała, bo pełny dzień tworzy 2 td-ki, liczba orderów != colspan
                    print colspan, order
                """
                orders[floor.number][room.name] = room_description

        context['all_houses'] = all_houses
        context['house'] = house
        context['floors'] = floors
        context['orders'] = orders
        context['date_range'] = [d1 + timedelta(n) for n in xrange(date_range)]
        return context


class ClosePopupMixin(object):
    def post(self, request, *args, **kwargs):
        response = super(ClosePopupMixin, self).post(request, *args, **kwargs)
        form = self.get_form(self.form_class)
        if not form.is_valid():
            return response
        return HttpResponse('''<script type="text/javascript">
            window.opener.location.reload();
            window.close();
        </script>''')


class OrderEdit(ClosePopupMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'popup_edit.html'


class OrderCreate(ClosePopupMixin, CreateView):
    model = Order
    form_class = OrderCreateForm
    template_name = "client/popup_create.html"

    def get_form_kwargs(self):
        kwargs = super(OrderCreate, self).get_form_kwargs()
        kwargs['arr_date'] = self.request.GET.get('arr_date')
        kwargs['room_id'] = self.request.GET.get('room_id')
        return kwargs
