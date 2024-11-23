from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DiceRollViewSet

router = DefaultRouter()
router.register(r'dice-rolls', DiceRollViewSet)

app_name = 'mechanics'

urlpatterns = [
    # API URLs
    path('api/', include(router.urls)),
]