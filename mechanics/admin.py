from django.contrib import admin
from .models import DiceRoll, Encounter, Loot

@admin.register(DiceRoll)
class DiceRollAdmin(admin.ModelAdmin):
    list_display = ('user', 'campaign', 'roll_type', 'result', 'timestamp')
    search_fields = ('user__username', 'campaign__name', 'roll_type', 'result')
    list_filter = ('roll_type', 'timestamp', 'campaign')