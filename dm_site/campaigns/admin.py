from django.contrib import admin
from .models import Campaign, Session

class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'status', 'created_at')
    search_fields = ('name', 'owner__username')
    list_filter = ('status', 'created_at')

class SessionAdmin(admin.ModelAdmin):
    list_display = ('campaign', 'date', 'time', 'created_at')
    search_fields = ('campaign__name',)
    list_filter = ('date', 'campaign__status')

admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Session, SessionAdmin)
