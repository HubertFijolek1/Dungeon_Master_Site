from django import forms
from .models import Encounter

class EncounterForm(forms.ModelForm):
    class Meta:
        model = Encounter
        fields = ['name', 'description', 'difficulty', 'monsters']
        widgets = {
            'monsters': forms.CheckboxSelectMultiple(),
        }