# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url, handler404
from django.contrib import admin

from hotelix.views import EasyHome

urlpatterns = patterns('',
    url(r'^$', EasyHome.as_view()),
    url(r'^dja/', include(admin.site.urls)),
    url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/', 'hotelix.views.logout_view'),
    url(r'^structure/', include(('structure.urls', 'structure', 'structure'))),
    url(r'^client/', include(('client.urls', 'client', 'client'))),
    url(r'^services/', include(('services.urls', 'services', 'services'))),
)
