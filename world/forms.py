from django import forms
from .models import Map, Location, Lore, TimelineEvent

class MapForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = ['name', 'image']

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'description', 'map', 'coordinates']

class LoreForm(forms.ModelForm):
    class Meta:
        model = Lore
        fields = ['title', 'content', 'related_location']

class TimelineEventForm(forms.ModelForm):
    class Meta:
        model = TimelineEvent
        fields = ['date', 'description', 'related_lore']