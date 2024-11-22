from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MapViewSet, LocationViewSet, LoreViewSet, TimelineEventViewSet

router = DefaultRouter()
router.register(r'maps', MapViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'lore', LoreViewSet)
router.register(r'timeline-events', TimelineEventViewSet)

app_name = 'world'

urlpatterns = [
    path('api/', include(router.urls)),
]