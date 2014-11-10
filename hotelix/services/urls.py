# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from services.views import MealTypeList, ServiceTypeList, MealTypeEdit,\
    ServiceTypeEdit, MealTypeCreate, ServiceTypeCreate, MealTypeDelete,\
    ServiceTypeDelete

urlpatterns = [
    url(r'^mealtype/$', MealTypeList.as_view(), name='mealtype_list'),
    url(r'^mealtype/(?P<pk>[0-9]+)/$', MealTypeEdit.as_view(), name='mealtype_edit'),
    url(r'^mealtype/create/$', MealTypeCreate.as_view(), name='mealtype_create'),
    url(r'^mealtype/(?P<pk>[0-9]+)/delete/$', MealTypeDelete.as_view(), name='mealtype_delete'),

    url(r'^servicetype/$', ServiceTypeList.as_view(), name='servicetype_list'),
    url(r'^servicetype/(?P<pk>[0-9]+)/$', ServiceTypeEdit.as_view(), name='servicetype_edit'),
    url(r'^servicetype/create/$', ServiceTypeCreate.as_view(), name='servicetype_create'),
    url(r'^servicetype/(?P<pk>[0-9]+)/delete/$', ServiceTypeDelete.as_view(), name='servicetype_delete'),
]