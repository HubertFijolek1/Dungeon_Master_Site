from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MapViewSet, LocationViewSet, LoreViewSet, TimelineEventViewSet,
    MapListView, MapDetailView, MapCreateView,
)

router = DefaultRouter()
router.register(r'maps', MapViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'lore', LoreViewSet)
router.register(r'timeline-events', TimelineEventViewSet)

app_name = 'world'

urlpatterns = [
    path('api/', include(router.urls)),

# Map URLs
    path('maps/', MapListView.as_view(), name='map_list'),
    path('maps/<int:pk>/', MapDetailView.as_view(), name='map_detail'),
    path('maps/create/', MapCreateView.as_view(), name='map_create'),
]