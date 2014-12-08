# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from hotelix.views import SuccessMixin,compute_lightness
from structure.forms import FloorForm, ChamberForm, RoomForm
from structure.models import House, Floor, Chamber, Room


class StructureMixin(object):
    bs_length = None
    bs_house_id = None
    bs_floor_id = None
    bs_room_id = None
    bs_house_prefix = None
    bs_floor_prefix = None
    bs_room_prefix = None
    is_chamber = False
    
    def get(self, request, *args, **kwargs):
        if not self.bs_length:
            raise NotImplementedError(u"Brak self.bs_length")
        if self.bs_length > 1 and not self.bs_house_prefix:
            raise NotImplementedError(u"Brak self.bs_house_prefix")
        if self.bs_length > 3 and not self.bs_floor_prefix:
            raise NotImplementedError(u"Brak self.bs_floor_prefix")
        if self.bs_length > 5 and not self.bs_room_prefix:
            raise NotImplementedError(u"Brak self.bs_room_prefix")
        self.bs_house_id = self.kwargs.get(self.bs_house_prefix, None)
        self.bs_floor_id = self.kwargs.get(self.bs_floor_prefix, None)
        self.bs_room_id = self.kwargs.get(self.bs_room_prefix, None)
        return super(StructureMixin, self).get(request, *args, **kwargs)

    def get_breadcrumbs(self):
        bs = [
            {'url':reverse_lazy('structure:house_list'), 'name': u'Domy'},
            {'url':reverse_lazy('structure:house_edit', args=[self.bs_house_id]),
             'name': u'Edycja domu'},
            {'url':reverse_lazy('structure:chamber_list', args=[self.bs_house_id]),
             'name': u'Pomieszczenia'},
        ] if self.is_chamber else [ 
            {'url':reverse_lazy('structure:house_list'), 'name': u'Domy'},
            {'url':reverse_lazy('structure:house_edit', args=[self.bs_house_id]),
             'name': u'Edycja domu'},
            {'url':reverse_lazy('structure:floor_list', args=[self.bs_house_id]),
             'name': u'Piętra'},
            {'url':reverse_lazy('structure:floor_edit',
                                args=[self.bs_house_id, self.bs_floor_id]),
             'name': u'Edycja piętra'},
            {'url':reverse_lazy('structure:room_list',
                                args=[self.bs_house_id, self.bs_floor_id]),
             'name': u'Pokoje'},
            {'url':reverse_lazy('structure:room_edit',
                                args=[self.bs_house_id, self.bs_floor_id, self.bs_room_id]),
             'name': u'Edycja pokoju'},
        ]
        return compute_lightness(bs[:self.bs_length])


""" HOUSE model """
class HouseList(StructureMixin, ListView):
    model = House
    extra_image = 'img/house.png'
    bs_length = 1


class HouseCreate(StructureMixin, CreateView):
    model = House
    success_url = reverse_lazy('structure:house_list')
    bs_length = 1


class HouseEdit(StructureMixin, SuccessMixin, UpdateView):
    model = House
    template_name = "edit.html"
    bs_length = 1


class HouseDelete(StructureMixin, DeleteView):
    model = House
    success_url = reverse_lazy('structure:house_list')
    bs_length = 2
    bs_house_prefix = 'pk'
    


""" FLOOR model """
class FloorList(StructureMixin, ListView):
    model = Floor
    extra_image = 'img/floor.png'
    bs_length = 3
    bs_house_prefix = 'house_id'

    def get_queryset(self):
        house_id = self.kwargs['house_id']
        return Floor.objects.filter(house_id=house_id)

    def get_context_data(self, **kwargs):
        context = super(FloorList, self).get_context_data(**kwargs)
        context['house_id'] = self.kwargs['house_id']
        context['house_name'] =\
            House.objects.get(pk=self.kwargs['house_id']).name
        return context


class FloorEdit(StructureMixin, SuccessMixin, UpdateView):
    model = Floor
    template_name = 'edit.html'
    form_class = FloorForm
    bs_length = 3
    bs_house_prefix = 'house_id'

    def get_form_kwargs(self):
        kwargs = super(FloorEdit, self).get_form_kwargs()
        kwargs['house_id'] = kwargs['instance'].house.id
        return kwargs


class FloorCreate(StructureMixin, CreateView):
    template_name = "create.html"
    model = Floor
    form_class = FloorForm
    bs_length = 3
    bs_house_prefix = 'house_id'
    
    def get_form_kwargs(self):
        kwargs = super(FloorCreate, self).get_form_kwargs()
        # rewrite house_id from URL to form
        kwargs['house_id'] = self.kwargs['house_id']
        return kwargs

    def get_success_url(self):
        return reverse_lazy('structure:floor_list', args=[self.kwargs['house_id']])


class FloorDelete(StructureMixin, DeleteView):
    template_name = 'delete.html'
    model = Floor
    bs_length = 4
    bs_house_prefix = 'house_id'
    bs_floor_prefix = 'pk'

    def get_success_url(self):
        return reverse_lazy('structure:floor_list', args=[self.kwargs['house_id']])

    def get_discard_url(self):
        return self.get_success_url()
    discard_url = property(get_discard_url)


""" ROOM model """
class RoomList(StructureMixin, ListView):
    model = House
    extra_image = 'img/room.png'
    bs_length = 5
    bs_house_prefix = 'house_id'
    bs_floor_prefix = 'floor_id'
    
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


class RoomCreate(StructureMixin, CreateView):
    template_name = "create.html"
    model = Room
    form_class = RoomForm
    bs_length = 5
    bs_house_prefix = 'house_id'
    bs_floor_prefix = 'floor_id'
    
    def get_form_kwargs(self):
        kwargs = super(RoomCreate, self).get_form_kwargs()
        kwargs['floor_id'] = self.kwargs['floor_id']
        return kwargs

    def get_success_url(self):
        kw = self.kwargs
        return reverse_lazy('structure:room_list', args=[kw['house_id'],
                                                         kw['floor_id']])


class RoomEdit(StructureMixin, SuccessMixin, UpdateView):
    model = Room
    template_name = 'edit.html'
    form_class = RoomForm
    bs_length = 5
    bs_house_prefix = 'house_id'
    bs_floor_prefix = 'floor_id'
    
    def get_form_kwargs(self):
        kwargs = super(RoomEdit, self).get_form_kwargs()
        kwargs['floor_id'] = kwargs['instance'].floor.id
        return kwargs


class RoomDelete(StructureMixin, DeleteView):
    template_name = 'delete.html'
    model = Room
    bs_length = 6
    bs_house_prefix = 'house_id'
    bs_floor_prefix = 'floor_id'
    bs_room_prefix = 'pk'

    def get_success_url(self):
        kw = self.kwargs
        return reverse_lazy('structure:room_list', args=[kw['house_id'],
                                                         kw['floor_id']])

    def get_discard_url(self):
        return self.get_success_url()
    discard_url = property(get_discard_url)


""" CHAMBER model """
class ChamberList(StructureMixin, ListView):
    model = Floor
    bs_length = 3
    bs_house_prefix = 'house_id'
    is_chamber = True

    def get_queryset(self):
        house_id = self.kwargs['house_id']
        return Chamber.objects.filter(house_id=house_id)

    def get_context_data(self, **kwargs):
        context = super(ChamberList, self).get_context_data(**kwargs)
        context['house_id'] = self.kwargs['house_id']
        context['house_name'] =\
            House.objects.get(pk=self.kwargs['house_id']).name
        return context


class ChamberEdit(StructureMixin, SuccessMixin, UpdateView):
    template_name = 'edit.html'
    model = Chamber
    form_class = ChamberForm
    bs_length = 3
    bs_house_prefix = 'house_id'
    is_chamber = True

    def get_form_kwargs(self):
        kwargs = super(ChamberEdit, self).get_form_kwargs()
        kwargs['house_id'] = kwargs['instance'].house.id
        return kwargs


class ChamberCreate(StructureMixin, CreateView):
    template_name = "create.html"
    model = Chamber
    form_class = ChamberForm
    bs_length = 3
    bs_house_prefix = 'house_id'
    is_chamber = True
    
    def get_form_kwargs(self):
        kwargs = super(ChamberCreate, self).get_form_kwargs()
        # rewrite house_id from URL to form
        kwargs['house_id'] = self.kwargs['house_id']
        return kwargs

    def get_success_url(self):
        return reverse_lazy('structure:chamber_list', args=[self.kwargs['house_id']])


class ChamberDelete(StructureMixin, DeleteView):
    template_name = 'delete.html'
    model = Chamber
    bs_length = 3
    bs_house_prefix = 'house_id'
    is_chamber = True

    def get_success_url(self):
        return reverse_lazy('structure:chamber_list', args=[self.kwargs['house_id']])

    def get_discard_url(self):
        return self.get_success_url()
    discard_url = property(get_discard_url)
