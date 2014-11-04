# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

#from structure.views import *
from structure.views import HouseList, FloorList

urlpatterns = [
    url(r'^houses/$', HouseList.as_view(), name='house_list'),
    url(r'^houses/(?P<house_id>[0-9]+)/list/$', FloorList.as_view(), name='floor_list'),
]