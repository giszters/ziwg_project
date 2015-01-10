# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from hotelix.views import SuccessMixin, PermMixin
from services.forms import MealOrderForm, ServiceOrderForm
from services.models import MealType, ServiceType, MealOrder, ServiceOrder


""" MEAL_TYPE model"""
class MealTypeList(PermMixin, ListView):
    model = MealType
    template_name = 'services/type_list.html'
    # My extra fields
    view_name = u"Lista posiłków"
    create_url = reverse_lazy('services:mealtype_create')
    perm_name = 'change_mealtype'

    def get_context_data(self, **kwargs):
        context = super(MealTypeList, self).get_context_data(**kwargs)
        return context


class MealTypeEdit(PermMixin, SuccessMixin, UpdateView):
    model = MealType
    template_name = 'edit.html'
    perm_name = 'change_mealtype'


class MealTypeCreate(PermMixin, CreateView):
    model = MealType
    template_name = 'create.html'
    perm_name = 'add_mealtype'


class MealTypeDelete(PermMixin, DeleteView):
    model = MealType
    template_name = 'delete.html'
    delete_arg = 'services:mealtype_delete'
    discard_url = success_url = reverse_lazy('services:mealtype_list')
    perm_name = 'delete_mealtype'


""" MEAL_ORDER model """
class MealOrderList(PermMixin, ListView):
    model = MealOrder
    template_name = 'services/meal_order_list.html'
    create_url = reverse_lazy('services:mealorder_create')
    perm_name = 'change_mealorder'

    def get_queryset(self):
        """ The youngest will be first on the list """
        return MealOrder.objects.order_by('-id')


class MealOrderEdit(PermMixin, SuccessMixin, UpdateView):
    model = MealOrder
    template_name = 'edit.html'
    form_class = MealOrderForm
    perm_name = 'change_mealorder'


class MealOrderDelete(PermMixin, DeleteView):
    model = MealOrder
    template_name = 'delete.html'
    delete_arg = 'services:mealorder_delete'
    discard_url = success_url = reverse_lazy('services:mealorder_list')
    perm_name = 'delete_mealorder'


class MealOrderCreate(PermMixin, CreateView):
    model = MealOrder
    template_name = 'create.html'
    form_class = MealOrderForm
    perm_name = 'add_mealorder'


""" SERVICE_TYPE model"""
class ServiceTypeList(PermMixin, ListView):
    model = ServiceType
    template_name = 'services/type_list.html'
    view_name = u"Lista usług"
    create_url = reverse_lazy('services:servicetype_create')
    perm_name = 'change_servicetype'


class ServiceTypeEdit(PermMixin, SuccessMixin, UpdateView):
    model = ServiceType
    template_name = "edit.html"
    perm_name = 'change_servicetype'


class ServiceTypeCreate(PermMixin, CreateView):
    model = ServiceType
    template_name = 'create.html'
    perm_name = 'add_servicetype'


class ServiceTypeDelete(PermMixin, DeleteView):
    model = ServiceType
    template_name = 'delete.html'
    delete_arg = 'services:servicetype_delete'
    discard_url = success_url = reverse_lazy('services:servicetype_list')
    perm_name = 'delete_servicetype'


""" SERVICE_ORDER model """
class ServiceOrderList(PermMixin, ListView):
    model = ServiceOrder
    template_name = 'services/service_order_list.html'
    create_url = reverse_lazy('services:serviceorder_create')
    perm_name = 'change_serviceorder'

    def get_queryset(self):
        """ The youngest will be first on the list """
        return ServiceOrder.objects.order_by('-id')


class ServiceOrderEdit(PermMixin, SuccessMixin, UpdateView):
    model = ServiceOrder
    template_name = 'edit.html'
    form_class = ServiceOrderForm
    perm_name = 'change_serviceorder'


class ServiceOrderDelete(PermMixin, DeleteView):
    model = ServiceOrder
    template_name = 'delete.html'
    delete_arg = 'services:serviceorder_delete'
    discard_url = success_url = reverse_lazy('services:serviceorder_list')
    perm_name = 'delete_serviceorder'


class ServiceOrderCreate(PermMixin, CreateView):
    model = ServiceOrder
    template_name = 'create.html'
    form_class = ServiceOrderForm
    perm_name = 'add_serviceorder'
