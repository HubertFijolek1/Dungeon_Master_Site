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

    def clean_coordinates(self):
        coords = self.cleaned_data.get('coordinates')
        if coords:
            try:
                lat_str, lon_str = coords.split(',')
                lat = float(lat_str.strip())
                lon = float(lon_str.strip())
                if not (-90 <= lat <= 90 and -180 <= lon <= 180):
                    raise forms.ValidationError("Invalid latitude or longitude values.")
            except ValueError:
                raise forms.ValidationError("Coordinates must be in the format 'latitude,longitude'.")
        return coords

class LoreForm(forms.ModelForm):
    class Meta:
        model = Lore
        fields = ['title', 'content', 'related_location']

class TimelineEventForm(forms.ModelForm):
    class Meta:
        model = TimelineEvent
        fields = ['date', 'description', 'related_lore']