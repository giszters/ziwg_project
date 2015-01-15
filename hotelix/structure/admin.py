from django.contrib import admin

from structure.models import House, Floor, Room, Chamber

class FloorAdmin(admin.ModelAdmin):
    list_display = ('number', 'house')

admin.site.register(House)
#admin.site.register(Floor, FloorAdmin)
#admin.site.register(Room)
#admin.site.register(Chamber)
