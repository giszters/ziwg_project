# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from hotelix.views import SuccessMixin,compute_lightness
from structure.forms import FloorForm, ChamberForm, RoomForm
from structure.models import House, Floor, Chamber, Room


""" HOUSE model """
class HouseList(ListView):
    model = House
    extra_image = 'img/house.png'

    def get_breadcrumbs(self):
        urls = [
            {'url':'#', 'name': u'Domy'},
            {'url':'#', 'name': u'Edycja domu'},
            {'url':'#', 'name': u'Piętra'},
            {'url':'#', 'name': u'Edycja piętra'},
            {'url':'#', 'name': u'Pokoje'},
            {'url':'#', 'name': u'Edycja pokoju'},
        ]
        compute_lightness(urls)
        return urls


class HouseCreate(CreateView):
    model = House
    success_url = reverse_lazy('structure:house_list')


class HouseEdit(SuccessMixin, UpdateView):
    model = House
    template_name = "edit.html"


class HouseDelete(DeleteView):
    model = House
    success_url = reverse_lazy('structure:house_list')


""" FLOOR model """
class FloorList(ListView):
    model = Floor
    extra_image = 'img/floor.png'

    def get_queryset(self):
        house_id = self.kwargs['house_id']
        return Floor.objects.filter(house_id=house_id)

    def get_context_data(self, **kwargs):
        context = super(FloorList, self).get_context_data(**kwargs)
        context['house_id'] = self.kwargs['house_id']
        context['house_name'] =\
            House.objects.get(pk=self.kwargs['house_id']).name
        return context


class FloorEdit(SuccessMixin, UpdateView):
    model = Floor
    template_name = 'edit.html'
    form_class = FloorForm

    def get_form_kwargs(self):
        kwargs = super(FloorEdit, self).get_form_kwargs()
        kwargs['house_id'] = kwargs['instance'].house.id
        return kwargs


class FloorCreate(CreateView):
    template_name = "create.html"
    model = Floor
    form_class = FloorForm
    
    def get_form_kwargs(self):
        kwargs = super(FloorCreate, self).get_form_kwargs()
        # rewrite house_id from URL to form
        kwargs['house_id'] = self.kwargs['house_id']
        return kwargs

    def get_success_url(self):
        return reverse_lazy('structure:floor_list', args=[self.kwargs['house_id']])


class FloorDelete(DeleteView):
    template_name = 'delete.html'
    model = Floor

    def get_success_url(self):
        return reverse_lazy('structure:floor_list', args=[self.kwargs['house_id']])

    def get_discard_url(self):
        return self.get_success_url()
    discard_url = property(get_discard_url)


""" ROOM model """
class RoomList(ListView):
    model = House
    extra_image = 'img/room.png'
    
    def get_queryset(self):
        floor_id = self.kwargs['floor_id']
        return Room.objects.filter(floor_id=floor_id)

    def get_context_data(self, **kwargs):
        context = super(RoomList, self).get_context_data(**kwargs)
        context['floor_id'] = self.kwargs['floor_id']
        context['house_id'] = self.kwargs['house_id']
        context['floor_number'] =\
            Floor.objects.get(pk=self.kwargs['floor_id']).number
        return context


class RoomCreate(CreateView):
    template_name = "create.html"
    model = Room
    form_class = RoomForm
    
    def get_form_kwargs(self):
        kwargs = super(RoomCreate, self).get_form_kwargs()
        kwargs['floor_id'] = self.kwargs['floor_id']
        return kwargs

    def get_success_url(self):
        kw = self.kwargs
        return reverse_lazy('structure:room_list', args=[kw['house_id'],
                                                         kw['floor_id']])


class RoomEdit(SuccessMixin, UpdateView):
    model = Room
    template_name = 'edit.html'
    form_class = RoomForm
    
    def get_form_kwargs(self):
        kwargs = super(RoomEdit, self).get_form_kwargs()
        kwargs['floor_id'] = kwargs['instance'].floor.id
        return kwargs


class RoomDelete(DeleteView):
    template_name = 'delete.html'
    model = Room

    def get_success_url(self):
        kw = self.kwargs
        return reverse_lazy('structure:room_list', args=[kw['house_id'],
                                                         kw['floor_id']])

    def get_discard_url(self):
        return self.get_success_url()
    discard_url = property(get_discard_url)


""" CHAMBER model """
class ChamberList(ListView):
    model = Floor

    def get_queryset(self):
        house_id = self.kwargs['house_id']
        return Chamber.objects.filter(house_id=house_id)

    def get_context_data(self, **kwargs):
        context = super(ChamberList, self).get_context_data(**kwargs)
        context['house_id'] = self.kwargs['house_id']
        context['house_name'] =\
            House.objects.get(pk=self.kwargs['house_id']).name
        return context


class ChamberEdit(SuccessMixin, UpdateView):
    template_name = 'edit.html'
    model = Chamber
    form_class = ChamberForm

    def get_form_kwargs(self):
        kwargs = super(ChamberEdit, self).get_form_kwargs()
        kwargs['house_id'] = kwargs['instance'].house.id
        return kwargs


class ChamberCreate(CreateView):
    template_name = "create.html"
    model = Chamber
    form_class = ChamberForm
    
    def get_form_kwargs(self):
        kwargs = super(ChamberCreate, self).get_form_kwargs()
        # rewrite house_id from URL to form
        kwargs['house_id'] = self.kwargs['house_id']
        return kwargs

    def get_success_url(self):
        return reverse_lazy('structure:chamber_list', args=[self.kwargs['house_id']])


class ChamberDelete(DeleteView):
    template_name = 'delete.html'
    model = Chamber

    def get_success_url(self):
        return reverse_lazy('structure:chamber_list', args=[self.kwargs['house_id']])

    def get_discard_url(self):
        return self.get_success_url()
    discard_url = property(get_discard_url)
