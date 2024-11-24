from django import forms
from .models import Encounter, Loot

class EncounterForm(forms.ModelForm):
    class Meta:
        model = Encounter
        fields = ['name', 'description', 'difficulty', 'monsters']
        widgets = {
            'monsters': forms.CheckboxSelectMultiple(),
        }

class LootForm(forms.ModelForm):
    class Meta:
        model = Loot
        fields = ['name', 'description', 'type', 'value', 'encounter']