# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from hotelix.views import SuccessMixin
from services.models import MealType, ServiceType


""" MEAL_TYPE model"""
class MealTypeList(ListView):
    model = MealType
    template_name = 'services/type_list.html'
    # My extra fields
    view_name = u"Lista posiłków"
    create_url = reverse_lazy('services:mealtype_create')


    def get_context_data(self, **kwargs):
        context = super(MealTypeList, self).get_context_data(**kwargs)
        #import ipdb; ipdb.set_trace()
        return context



class MealTypeEdit(SuccessMixin, UpdateView):
    model = MealType
    template_name = 'edit.html'


class MealTypeCreate(CreateView):
    model = MealType
    template_name = 'create.html'


class MealTypeDelete(DeleteView):
    model = MealType
    template_name = 'delete.html'
    delete_arg = 'services:mealtype_delete'
    discard_url = success_url = reverse_lazy('services:mealtype_list')


""" SERVICE_TYPE model"""
class ServiceTypeList(ListView):
    model = ServiceType
    template_name = 'services/type_list.html'
    view_name = u"Lista usług"
    create_url = reverse_lazy('services:servicetype_create')


class ServiceTypeEdit(SuccessMixin, UpdateView):
    model = ServiceType
    template_name = "edit.html"


class ServiceTypeCreate(CreateView):
    model = ServiceType
    template_name = 'create.html'


class ServiceTypeDelete(DeleteView):
    model = ServiceType
    template_name = 'delete.html'
    delete_arg = 'services:servicetype_delete'
    discard_url = success_url = reverse_lazy('services:servicetype_list')