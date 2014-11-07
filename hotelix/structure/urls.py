# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

#from structure.views import *  # But I want to see all classes
from structure.views import HouseList, FloorList, HouseCreate, HouseEdit, HouseDelete

urlpatterns = [
    url(r'^houses/$', HouseList.as_view(), name='house_list'),
    url(r'^houses/create/$', HouseCreate.as_view(), name='house_create'),
    url(r'^houses/(?P<pk>[0-9]+)/edit/$', HouseEdit.as_view(), name='house_edit'),
    url(r'^houses/(?P<pk>[0-9]+)/delete/$', HouseDelete.as_view(), name='house_delete'),
    
    url(r'^houses/(?P<house_id>[0-9]+)/list/$', FloorList.as_view(), name='floor_list'),
]