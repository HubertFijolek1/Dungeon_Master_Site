from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MapViewSet, LocationViewSet

router = DefaultRouter()
router.register(r'maps', MapViewSet)
router.register(r'locations', LocationViewSet)

app_name = 'world'

urlpatterns = [
    path('api/', include(router.urls)),
]