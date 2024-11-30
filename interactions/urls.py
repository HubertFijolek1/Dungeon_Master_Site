from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, ForumPostViewSet, PollViewSet, PollVoteViewSet, MessageListView, MessageDetailView, MessageCreateView,ForumPostListView, ForumPostDetailView, ForumPostCreateView,

router = DefaultRouter()
router.register(r'messages', MessageViewSet, basename='message')
router.register(r'forum-posts', ForumPostViewSet, basename='forum-post')
router.register(r'polls', PollViewSet, basename='poll')
router.register(r'poll-votes', PollVoteViewSet, basename='poll-vote')


app_name = 'interactions'

urlpatterns = [
    path('api/', include(router.urls)),
]


urlpatterns += [
    # Message URLs
    path('messages/', MessageListView.as_view(), name='message_list'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('messages/compose/', MessageCreateView.as_view(), name='message_create'),
]

urlpatterns += [
    # Forum Post URLs
    path('forum-posts/', ForumPostListView.as_view(), name='forum_post_list'),
    path('forum-posts/<int:pk>/', ForumPostDetailView.as_view(), name='forum_post_detail'),
    path('forum-posts/create/', ForumPostCreateView.as_view(), name='forum_post_create'),
]