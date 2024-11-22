from rest_framework import viewsets, permissions
from .models import Map, Location, Lore
from .serializers import MapSerializer, LocationSerializer, LoreSerializer

class MapViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LoreViewSet(viewsets.ModelViewSet):
    queryset = Lore.objects.all()
    serializer_class = LoreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]