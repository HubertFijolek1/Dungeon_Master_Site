from django import forms
from .models import Encounter, Loot

class EncounterForm(forms.ModelForm):
    class Meta:
        model = Encounter
        fields = ['name', 'description', 'monsters']
        widgets = {
            'monsters': forms.CheckboxSelectMultiple(),
        }

    def clean(self):
        cleaned_data = super().clean()
        monsters = cleaned_data.get('monsters')
        if not monsters:
            raise forms.ValidationError("You must select at least one monster.")
        return cleaned_data

class LootForm(forms.ModelForm):
    class Meta:
        model = Loot
        fields = ['name', 'description', 'type', 'value', 'encounter']

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 0:
            raise forms.ValidationError("Value cannot be negative.")
        return value

class DiceRollForm(forms.Form):
    roll_type = forms.ChoiceField(choices=DiceRoll.ROLL_TYPES, initial='custom')
    expression = forms.CharField(max_length=50, help_text="Enter dice expression (e.g., '1d20+5')")