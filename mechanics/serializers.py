from rest_framework import serializers
from .models import DiceRoll, Encounter, Loot
from characters.models import Monster

class MonsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monster
        fields = '__all__'

class DiceRollSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = DiceRoll
        fields = '__all__'

class EncounterSerializer(serializers.ModelSerializer):
    monsters = MonsterSerializer(many=True, read_only=True)

    class Meta:
        model = Encounter
        fields = '__all__'

class LootSerializer(serializers.ModelSerializer):
    encounter = serializers.StringRelatedField()

    class Meta:
        model = Loot
        fields = '__all__'