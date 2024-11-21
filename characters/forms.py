from django import forms
from .models import Character, InventoryItem, Monster

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'character_type', 'attributes', 'backstory', 'campaign']

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'description', 'quantity']

class MonsterForm(forms.ModelForm):
    class Meta:
        model = Monster
        fields = ['name', 'stats', 'lore', 'campaign']