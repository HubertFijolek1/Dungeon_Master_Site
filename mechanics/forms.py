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

class DiceRollForm(forms.Form):
    roll_type = forms.ChoiceField(choices=DiceRoll.ROLL_TYPES, initial='custom')
    expression = forms.CharField(max_length=50, help_text="Enter dice expression (e.g., '1d20+5')")