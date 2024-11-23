from django.contrib import admin
from .models import DiceRoll, Encounter, Loot

@admin.register(DiceRoll)
class DiceRollAdmin(admin.ModelAdmin):
    list_display = ('user', 'campaign', 'roll_type', 'result', 'timestamp')
    search_fields = ('user__username', 'campaign__name', 'roll_type', 'result')
    list_filter = ('roll_type', 'timestamp', 'campaign')

@admin.register(Encounter)
class EncounterAdmin(admin.ModelAdmin):
    list_display = ('name', 'campaign', 'difficulty', 'created_at')
    search_fields = ('name', 'campaign__name')
    list_filter = ('difficulty', 'campaign')
    filter_horizontal = ('monsters',)