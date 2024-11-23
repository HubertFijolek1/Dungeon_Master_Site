from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DiceRollViewSet, EncounterViewSet

router = DefaultRouter()
router.register(r'dice-rolls', DiceRollViewSet)
router.register(r'encounters', EncounterViewSet)

app_name = 'mechanics'

urlpatterns = [
    # API URLs
    path('api/', include(router.urls)),
]