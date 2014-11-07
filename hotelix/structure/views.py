# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from structure.models import House, Floor


class HouseList(ListView):
    model = House


class FloorList(ListView):
    model = Floor

    def get_queryset(self):
        house_id = self.kwargs['house_id']
        return Floor.objects.filter(house_id=house_id)

    def get_context_data(self, **kwargs):
        context = super(FloorList, self).get_context_data(**kwargs)
        context['house_name'] =\
            House.objects.get(pk=self.kwargs['house_id']).name
        return context


class HouseCreate(CreateView):
    model = House
    success_url = reverse_lazy('structure:house_list')


class HouseEdit(UpdateView):
    model = House
    # I don't want the same template for create and update
    # so I change below variable 
    template_name_suffix = "_edit"
    
    def get_success_url(self):
        url = super(HouseEdit, self).get_success_url()
        url += "?success=1"  # And jQuery make magic (look at the base.html)
        return url


class HouseDelete(DeleteView):
    model = House
    success_url = reverse_lazy('structure:house_list')
