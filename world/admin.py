from django.contrib import admin
from .models import Map, Location

@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'map', 'coordinates', 'created_at')
    search_fields = ('name', 'map__name')
    list_filter = ('map', 'created_at')