from rest_framework import serializers
from .models import DiceRoll, Encounter, Loot

class DiceRollSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiceRoll
        fields = '__all__'

class EncounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encounter
        fields = '__all__'

class LootSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loot
        fields = '__all__'