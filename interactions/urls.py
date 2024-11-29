from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, ForumPostViewSet, PollViewSet, PollVoteViewSet

router = DefaultRouter()
router.register(r'messages', MessageViewSet, basename='message')
router.register(r'forum-posts', ForumPostViewSet, basename='forum-post')
router.register(r'polls', PollViewSet, basename='poll')
router.register(r'poll-votes', PollVoteViewSet, basename='poll-vote')


app_name = 'interactions'

urlpatterns = [
    path('api/', include(router.urls)),
]


