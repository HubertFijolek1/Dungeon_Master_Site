from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MessageViewSet, ForumPostViewSet, PollViewSet, PollVoteViewSet,
    MessageListView, MessageDetailView, MessageCreateView,
    ForumPostListView, ForumPostDetailView, ForumPostCreateView,
    PollListView, PollDetailView, PollCreateView, vote_poll, chat_view,
)
from django.contrib.auth.decorators import login_required

router = DefaultRouter()
router.register(r'messages', MessageViewSet, basename='message')
router.register(r'forum-posts', ForumPostViewSet, basename='forum-post')
router.register(r'polls', PollViewSet, basename='poll')
router.register(r'poll-votes', PollVoteViewSet, basename='poll-vote')

app_name = 'interactions'

urlpatterns = [
    path('api/', include(router.urls)),

    # Message URLs
    path('messages/', MessageListView.as_view(), name='message_list'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('messages/compose/', MessageCreateView.as_view(), name='message_create'),

    # Forum Post URLs
    path('forum-posts/', ForumPostListView.as_view(), name='forum_post_list'),
    path('forum-posts/<int:pk>/', ForumPostDetailView.as_view(), name='forum_post_detail'),
    path('forum-posts/create/', ForumPostCreateView.as_view(), name='forum_post_create'),

    # Poll URLs
    path('polls/', PollListView.as_view(), name='poll_list'),
    path('polls/<int:pk>/', PollDetailView.as_view(), name='poll_detail'),
    path('polls/create/', PollCreateView.as_view(), name='poll_create'),
    path('polls/<int:poll_id>/vote/', login_required(vote_poll), name='vote_poll'),

    # Chat URL
    path('chat/', login_required(chat_view), name='chat'),
]