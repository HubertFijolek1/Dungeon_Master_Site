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