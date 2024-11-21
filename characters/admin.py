from django.contrib import admin
from .models import Character, InventoryItem, Monster

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'character_type', 'campaign', 'created_at')
    search_fields = ('name', 'campaign__name')
    list_filter = ('character_type', 'campaign__status')

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'character', 'created_at')
    search_fields = ('name', 'character__name')
    list_filter = ('character__campaign__status',)

@admin.register(Monster)
class MonsterAdmin(admin.ModelAdmin):
    list_display = ('name', 'campaign', 'created_at')
    search_fields = ('name', 'campaign__name')
    list_filter = ('campaign__status', 'created_at')