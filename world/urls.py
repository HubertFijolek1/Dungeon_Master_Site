from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MapViewSet, LocationViewSet, LoreViewSet, TimelineEventViewSet,
    MapListView, MapDetailView, MapCreateView,
    LocationListView, LocationDetailView, LocationCreateView,
    LoreListView, LoreDetailView, LoreCreateView,
    TimelineEventListView, TimelineEventDetailView, TimelineEventCreateView,
)

router = DefaultRouter()
router.register(r'maps', MapViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'lore', LoreViewSet)
router.register(r'timeline-events', TimelineEventViewSet)

app_name = 'world'

urlpatterns = [
    # API URLs
    path('api/', include(router.urls)),

    # Map URLs
    path('maps/', MapListView.as_view(), name='map_list'),
    path('maps/<int:pk>/', MapDetailView.as_view(), name='map_detail'),
    path('maps/create/', MapCreateView.as_view(), name='map_create'),

    # Location URLs
    path('locations/', LocationListView.as_view(), name='location_list'),
    path('locations/<int:pk>/', LocationDetailView.as_view(), name='location_detail'),
    path('locations/create/', LocationCreateView.as_view(), name='location_create'),

    # Lore URLs
    path('lore/', LoreListView.as_view(), name='lore_list'),
    path('lore/<int:pk>/', LoreDetailView.as_view(), name='lore_detail'),
    path('lore/create/', LoreCreateView.as_view(), name='lore_create'),

    # TimelineEvent URLs
    path('timeline/', TimelineEventListView.as_view(), name='timelineevent_list'),
    path('timeline/<int:pk>/', TimelineEventDetailView.as_view(), name='timelineevent_detail'),
    path('timeline/create/', TimelineEventCreateView.as_view(), name='timelineevent_create'),
]