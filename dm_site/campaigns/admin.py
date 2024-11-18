from django.contrib import admin
from .models import Campaign

class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'status', 'created_at')
    search_fields = ('name', 'owner__username')
    list_filter = ('status', 'created_at')

admin.site.register(Campaign, CampaignAdmin)
