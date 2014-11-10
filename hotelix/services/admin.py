# -*- coding: utf-8 -*-
from django.contrib import admin

from services.models import MealOrder, MealType, ServiceOrder, ServiceType


admin.site.register(MealOrder)
admin.site.register(MealType)
admin.site.register(ServiceOrder)
admin.site.register(ServiceType)
