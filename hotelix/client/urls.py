# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

#from structure.views import *  # But I want to see all classes
from client.views import ClientList, ClientEdit, ClientCreate, ClientDelete,\
    OrderList, OrderEdit, OrderCreate

urlpatterns = [
    url(r'^client/$', ClientList.as_view(), name='client_list'),
    url(r'^client/(?P<pk>[0-9]+)/edit/$', ClientEdit.as_view(), name='client_edit'),
    url(r'^client/create/$', ClientCreate.as_view(), name='client_create'),
    url(r'^client/(?P<pk>[0-9]+)/delete/$', ClientDelete.as_view(), name='client_delete'),

    url(r'^order/$', OrderList.as_view(), name='order_list'),
    url(r'^order/(?P<pk>[0-9]+)/edit/$', OrderEdit.as_view(), name='order_edit'),
    url(r'^order/create/$', OrderCreate.as_view(), name='order_create'),
    #url(r'^houses/(?P<pk>[0-9]+)/edit/$', HouseEdit.as_view(), name='house_edit'),
]
