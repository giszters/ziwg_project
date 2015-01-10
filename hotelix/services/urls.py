# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from services.views import MealTypeList, ServiceTypeList, MealTypeEdit,\
    ServiceTypeEdit, MealTypeCreate, ServiceTypeCreate, MealTypeDelete,\
    ServiceTypeDelete, MealOrderList, MealOrderEdit, MealOrderDelete,\
    MealOrderCreate, ServiceOrderList, ServiceOrderEdit, ServiceOrderDelete,\
    ServiceOrderCreate

urlpatterns = [
    url(r'^mealtype/$', MealTypeList.as_view(), name='mealtype_list'),
    url(r'^mealtype/(?P<pk>[0-9]+)/$', MealTypeEdit.as_view(), name='mealtype_edit'),
    url(r'^mealtype/create/$', MealTypeCreate.as_view(), name='mealtype_create'),
    url(r'^mealtype/(?P<pk>[0-9]+)/delete/$', MealTypeDelete.as_view(), name='mealtype_delete'),

    url(r'^servicetype/$', ServiceTypeList.as_view(), name='servicetype_list'),
    url(r'^servicetype/(?P<pk>[0-9]+)/$', ServiceTypeEdit.as_view(), name='servicetype_edit'),
    url(r'^servicetype/create/$', ServiceTypeCreate.as_view(), name='servicetype_create'),
    url(r'^servicetype/(?P<pk>[0-9]+)/delete/$', ServiceTypeDelete.as_view(), name='servicetype_delete'),
    
    url(r'^mealorder/$', MealOrderList.as_view(), name='mealorder_list'),
    url(r'^mealorder/(?P<pk>[0-9]+)/$', MealOrderEdit.as_view(), name='mealorder_edit'),
    url(r'^mealorder/create/$', MealOrderCreate.as_view(), name='mealorder_create'),
    url(r'^mealorder/(?P<pk>[0-9]+)/delete/$', MealOrderDelete.as_view(), name='mealorder_delete'),
    
    url(r'^serviceorder/$', ServiceOrderList.as_view(), name='serviceorder_list'),
    url(r'^serviceorder/(?P<pk>[0-9]+)/$', ServiceOrderEdit.as_view(), name='serviceorder_edit'),
    url(r'^serviceorder/create/$', ServiceOrderCreate.as_view(), name='serviceorder_create'),
    url(r'^serviceorder/(?P<pk>[0-9]+)/delete/$', ServiceOrderDelete.as_view(), name='serviceorder_delete'),
]
