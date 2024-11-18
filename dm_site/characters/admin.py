from django.contrib import admin
from .models import Character, InventoryItem

class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'character_type', 'campaign', 'created_at')
    search_fields = ('name', 'campaign__name')
    list_filter = ('character_type', 'campaign__status')

class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'character', 'created_at')
    search_fields = ('name', 'character__name')
    list_filter = ('character__campaign__status',)

admin.site.register(Character, CharacterAdmin)
admin.site.register(InventoryItem, InventoryItemAdmin)
