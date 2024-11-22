from django import forms
from .models import Map, Lore

class LoreForm(forms.ModelForm):
    class Meta:
        model = Lore
        fields = ['title', 'content', 'related_location']

class MapForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = ['name', 'image']