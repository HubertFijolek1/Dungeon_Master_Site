from django.contrib import admin
from .models import Message, ForumPost, Poll, PollOption, PollVote

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'short_content', 'timestamp')
    search_fields = ('sender__username', 'receiver__username', 'content')
    list_filter = ('timestamp',)

    def short_content(self, obj):
        return obj.content[:50]
    short_content.short_description = 'Content'

@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'campaign', 'created_at')
    search_fields = ('title', 'content', 'author__username', 'campaign__name')
    list_filter = ('created_at', 'campaign')

class PollOptionInline(admin.TabularInline):
    model = PollOption
    extra = 1

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'campaign', 'created_at')
    search_fields = ('question', 'campaign__name')
    list_filter = ('created_at', 'campaign')
    inlines = [PollOptionInline]