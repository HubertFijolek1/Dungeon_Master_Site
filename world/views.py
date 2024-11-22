from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets, permissions
from .models import Map, Location, Lore, TimelineEvent
from .serializers import MapSerializer, LocationSerializer, LoreSerializer, TimelineEventSerializer
from .forms import MapForm, LocationForm, LoreForm, TimelineEventForm

# REST Framework ViewSets

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

# Django Views

# Map Views
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

# Location Views
class LocationListView(ListView):
    model = Location
    template_name = 'world/location_list.html'
    context_object_name = 'locations'

class LocationDetailView(DetailView):
    model = Location
    template_name = 'world/location_detail.html'
    context_object_name = 'location'

class LocationCreateView(LoginRequiredMixin, CreateView):
    model = Location
    form_class = LocationForm
    template_name = 'world/location_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

# Lore Views
class LoreListView(ListView):
    model = Lore
    template_name = 'world/lore_list.html'
    context_object_name = 'lore_entries'

class LoreDetailView(DetailView):
    model = Lore
    template_name = 'world/lore_detail.html'
    context_object_name = 'lore'

class LoreCreateView(LoginRequiredMixin, CreateView):
    model = Lore
    form_class = LoreForm
    template_name = 'world/lore_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

# TimelineEvent Views
class TimelineEventListView(ListView):
    model = TimelineEvent
    template_name = 'world/timelineevent_list.html'
    context_object_name = 'events'
    ordering = ['date']

class TimelineEventDetailView(DetailView):
    model = TimelineEvent
    template_name = 'world/timelineevent_detail.html'
    context_object_name = 'event'

class TimelineEventCreateView(LoginRequiredMixin, CreateView):
    model = TimelineEvent
    form_class = TimelineEventForm
    template_name = 'world/timelineevent_form.html'

    def form_valid(self, form):
        return super().form_valid(form)