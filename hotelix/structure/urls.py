# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

#from structure.views import *  # But I want to see all classes
from structure.views import HouseList, FloorList, HouseCreate, HouseEdit,\
    HouseDelete, FloorEdit, FloorCreate, FloorDelete, ChamberList, ChamberEdit, \
    ChamberCreate, ChamberDelete

urlpatterns = [
    url(r'^houses/$', HouseList.as_view(), name='house_list'),
    url(r'^houses/create/$', HouseCreate.as_view(), name='house_create'),
    url(r'^houses/(?P<pk>[0-9]+)/edit/$', HouseEdit.as_view(), name='house_edit'),
    url(r'^houses/(?P<pk>[0-9]+)/delete/$', HouseDelete.as_view(), name='house_delete'),
    
    url(r'^houses/(?P<house_id>[0-9]+)/list/$', FloorList.as_view(), name='floor_list'),
    url(r'^houses/(?P<house_id>[0-9]+)/create/$', FloorCreate.as_view(), name='floor_create'),
    url(r'^houses/(?P<house_id>[0-9]+)/(?P<pk>[0-9]+)/edit/$', FloorEdit.as_view(), name='floor_edit'),
    url(r'^houses/(?P<house_id>[0-9]+)/(?P<pk>[0-9]+)/delete/$', FloorDelete.as_view(), name='floor_delete'),
    
    url(r'^houses/(?P<house_id>[0-9]+)/chamberlist/$', ChamberList.as_view(), name='chamber_list'),
    url(r'^houses/(?P<house_id>[0-9]+)/chambercreate/$', ChamberCreate.as_view(), name='chamber_create'),
    url(r'^houses/(?P<house_id>[0-9]+)/(?P<pk>[0-9]+)/chmaberedit/$', ChamberEdit.as_view(), name='chamber_edit'),
    url(r'^houses/(?P<house_id>[0-9]+)/(?P<pk>[0-9]+)/chmaberdelete/$', ChamberDelete.as_view(), name='chamber_delete'),
]