from django.contrib import admin
from .models import Spell

@admin.register(Spell)
class SpellAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'school', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('level', 'school', 'created_at')