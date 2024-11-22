from rest_framework import serializers
from .models import Map, Location, Lore, TimelineEvent

class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class LoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lore
        fields = '__all__'

class TimelineEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimelineEvent
        fields = '__all__'