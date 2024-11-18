from django.contrib import admin
from .models import Character

class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'character_type', 'campaign', 'created_at')
    search_fields = ('name', 'campaign__name')
    list_filter = ('character_type', 'campaign__status')

admin.site.register(Character, CharacterAdmin)