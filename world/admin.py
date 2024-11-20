from django.contrib import admin
from .models import Map

class MapAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

admin.site.register(Map, MapAdmin)