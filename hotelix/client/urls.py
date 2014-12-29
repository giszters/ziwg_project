# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

#from structure.views import *  # But I want to see all classes
from client.views import ClientList, OrderList, OrderEdit

urlpatterns = [
    url(r'^client/$', ClientList.as_view(), name='client_list'),

    url(r'^order/$', OrderList.as_view(), name='order_list'),
    url(r'^order/(?P<pk>[0-9]+)/edit/$', OrderEdit.as_view(), name='order_edit')
    #url(r'^houses/(?P<pk>[0-9]+)/edit/$', HouseEdit.as_view(), name='house_edit'),
]
