from django.contrib import admin
from .models import Spell, Ability, Item

@admin.register(Spell)
class SpellAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'school', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('level', 'school', 'created_at')

@admin.register(Ability)
class AbilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'related_spell', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('type', 'created_at')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'rarity', 'value', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('type', 'rarity', 'created_at')