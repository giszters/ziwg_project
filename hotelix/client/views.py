# -*- coding: utf-8 -*-
from collections import OrderedDict
import datetime
from datetime import timedelta

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, \
    TemplateView

from client.forms import OrderForm
from client.models import Client, Order
#from hotelix.views import PopupMixin
from structure.models import House, Floor, Room


class ClientList(ListView):
    model = Client


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
                orders[floor.number][room.name] = room_description

        context['all_houses'] = all_houses
        context['house'] = house
        context['floors'] = floors
        context['orders'] = orders
        context['date_range'] = [d1 + timedelta(n) for n in xrange(date_range)]
        return context


class OrderEdit(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'popup_edit.html'

    def post(self, request, *args, **kwargs):
        response = super(OrderEdit, self).post(request, *args, **kwargs)
        form = self.get_form(self.form_class)
        if not form.is_valid():
            return response
        return HttpResponse('''<script type="text/javascript">
            window.opener.location.reload();
            window.close();
        </script>''')

