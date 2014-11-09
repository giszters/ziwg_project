# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'hotelix.views.home'),
    url(r'^dja/', include(admin.site.urls)),
    url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/', 'hotelix.views.logout_view'),
    url(r'^structure/', include(('structure.urls', 'structure', 'structure'))),
    url(r'^client/', include(('client.urls', 'client', 'client'))),
)
