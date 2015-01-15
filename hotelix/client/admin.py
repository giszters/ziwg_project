from django.contrib import admin

from client.models import Client, Order, Physician

admin.site.register(Client)
admin.site.register(Physician)
