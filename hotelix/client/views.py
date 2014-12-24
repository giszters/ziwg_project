# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from hotelix.views import SuccessMixin
from client.models import Client, Order


class ClientList(ListView):
    model = Client


## inherit also StructureMixin, SuccessMixin?
class OrderEdit(SuccessMixin, UpdateView):
    model = Order
    template_name = "edit.html"
    bs_length = 1


class OrderList(ListView):
    model = Order


class OrderCreate(ListView):
    model = Order
    template_name = 'create.html'


class OrderDelete(ListView):
    model = Order
    template_name = 'delete.html'
