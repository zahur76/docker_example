from distutils.command.build_clib import show_compilers
from django.contrib import admin
from django.contrib.gis import admin

from .models import Shop

@admin.register(Shop)
class MarkerAdmin(admin.OSMGeoAdmin):
    """Marker admin."""

    list_display = (
        "id",
        "name",
    )

