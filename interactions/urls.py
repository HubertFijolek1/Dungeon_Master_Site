from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet

router = DefaultRouter()
router.register(r'messages', MessageViewSet, basename='message')

app_name = 'interactions'

urlpatterns = [
    path('api/', include(router.urls)),
]