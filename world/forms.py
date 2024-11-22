from django import forms
from .models import Map, Lore, TimelineEvent

class TimelineEventForm(forms.ModelForm):
    class Meta:
        model = TimelineEvent
        fields = ['date', 'description', 'related_lore']

class LoreForm(forms.ModelForm):
    class Meta:
        model = Lore
        fields = ['title', 'content', 'related_location']

class MapForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = ['name', 'image']