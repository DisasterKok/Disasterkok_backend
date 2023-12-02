from django.contrib import admin

from region.models import Region


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'notification',
        'default',
        'onOff',
        'name',
        'address',
        'roadAdress',
        'zoneCode',
        'xCoordinate',
        'yCoordinate',
        'aliasType',
    )