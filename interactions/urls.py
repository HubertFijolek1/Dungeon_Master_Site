from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, ForumPostViewSet

router = DefaultRouter()
router.register(r'messages', MessageViewSet, basename='message')
router.register(r'forum-posts', ForumPostViewSet, basename='forum-post')

app_name = 'interactions'

urlpatterns = [
    path('api/', include(router.urls)),
]