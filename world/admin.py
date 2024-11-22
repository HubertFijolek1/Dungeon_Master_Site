from django.contrib import admin
from .models import Map, Location,Lore, TimelineEvent

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

@admin.register(Lore)
class LoreAdmin(admin.ModelAdmin):
    list_display = ('title', 'related_location', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)

    def related_location_name(self, obj):
        return obj.related_location.name if obj.related_location else 'N/A'
    related_location_name.short_description = 'Related Location'

@admin.register(TimelineEvent)
class TimelineEventAdmin(admin.ModelAdmin):
    list_display = ('date', 'short_description', 'related_lore', 'created_at')
    search_fields = ('description',)
    list_filter = ('date', 'created_at')

    def short_description(self, obj):
        return obj.description[:50]
    short_description.short_description = 'Description'