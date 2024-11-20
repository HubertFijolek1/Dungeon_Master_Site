from django import forms
from .models import Character, InventoryItem

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'character_type', 'attributes', 'backstory', 'campaign']

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'description', 'quantity']