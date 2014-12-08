# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from hotelix.views import SuccessMixin
from services.forms import MealOrderForm, ServiceOrderForm
from services.models import MealType, ServiceType, MealOrder, ServiceOrder


""" MEAL_TYPE model"""
class MealTypeList(ListView):
    model = MealType
    template_name = 'services/type_list.html'
    # My extra fields
    view_name = u"Lista posiłków"
    create_url = reverse_lazy('services:mealtype_create')

    def get_context_data(self, **kwargs):
        context = super(MealTypeList, self).get_context_data(**kwargs)
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


""" MEAL_ORDER model """
class MealOrderList(ListView):
    model = MealOrder
    template_name = 'services/meal_order_list.html'
    create_url = reverse_lazy('services:mealorder_create')

    def get_queryset(self):
        """ The youngest will be first on the list """
        return MealOrder.objects.order_by('-id')


class MealOrderEdit(SuccessMixin, UpdateView):
    model = MealOrder
    template_name = 'edit.html'
    form_class = MealOrderForm


class MealOrderDelete(DeleteView):
    model = MealOrder
    template_name = 'delete.html'
    delete_arg = 'services:mealorder_delete'
    discard_url = success_url = reverse_lazy('services:mealorder_list')


class MealOrderCreate(CreateView):
    model = MealOrder
    template_name = 'create.html'
    form_class = MealOrderForm


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


""" SERVICE_ORDER model """
class ServiceOrderList(ListView):
    model = ServiceOrder
    template_name = 'services/service_order_list.html'
    create_url = reverse_lazy('services:serviceorder_create')

    def get_queryset(self):
        """ The youngest will be first on the list """
        return ServiceOrder.objects.order_by('-id')


class ServiceOrderEdit(SuccessMixin, UpdateView):
    model = ServiceOrder
    template_name = 'edit.html'
    form_class = ServiceOrderForm


class ServiceOrderDelete(DeleteView):
    model = ServiceOrder
    template_name = 'delete.html'
    delete_arg = 'services:serviceorder_delete'
    discard_url = success_url = reverse_lazy('services:serviceorder_list')


class ServiceOrderCreate(CreateView):
    model = ServiceOrder
    template_name = 'create.html'
    form_class = ServiceOrderForm
