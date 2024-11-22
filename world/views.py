from rest_framework import viewsets, permissions
from .models import Map, Location, Lore, TimelineEvent
from .serializers import MapSerializer, LocationSerializer, LoreSerializer, TimelineEventSerializer
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MapForm


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

class TimelineEventViewSet(viewsets.ModelViewSet):
    queryset = TimelineEvent.objects.all()
    serializer_class = TimelineEventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MapListView(ListView):
    model = Map
    template_name = 'world/map_list.html'
    context_object_name = 'maps'

class MapDetailView(DetailView):
    model = Map
    template_name = 'world/map_detail.html'
    context_object_name = 'map'

class MapCreateView(LoginRequiredMixin, CreateView):
    model = Map
    form_class = MapForm
    template_name = 'world/map_form.html'

    def form_valid(self, form):
        return super().form_valid(form)