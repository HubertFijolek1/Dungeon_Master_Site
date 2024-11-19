from django.contrib import admin
from .models import Campaign, Session, Milestone, Participant

class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'status', 'created_at')
    search_fields = ('name', 'owner__username')
    list_filter = ('status', 'created_at')

class SessionAdmin(admin.ModelAdmin):
    list_display = ('campaign', 'date', 'time', 'created_at')
    search_fields = ('campaign__name',)
    list_filter = ('date', 'campaign__status')

class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('campaign', 'title', 'date', 'created_at')
    search_fields = ('campaign__name', 'title')
    list_filter = ('date',)

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('user', 'campaign', 'role', 'joined_at')
    search_fields = ('user__username', 'campaign__name')
    list_filter = ('role', 'joined_at')

admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Milestone, MilestoneAdmin)
admin.site.register(Participant, ParticipantAdmin)
