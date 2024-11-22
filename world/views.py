from rest_framework import viewsets, permissions
from .models import Map, Location
from .serializers import MapSerializer, LocationSerializer

class MapViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]