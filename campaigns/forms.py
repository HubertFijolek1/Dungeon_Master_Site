from django import forms
from .models import Campaign, Session, Milestone, Participant
from django.contrib.auth import get_user_model

User = get_user_model()

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['name', 'description', 'status']

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['date', 'time', 'notes']

class MilestoneForm(forms.ModelForm):
    class Meta:
        model = Milestone
        fields = ['title', 'description', 'date']

class ParticipantInviteForm(forms.Form):
    username = forms.CharField(max_length=150, help_text="Enter the username of the user to invite.")

    def __init__(self, *args, **kwargs):
        self.campaign = kwargs.pop('campaign')
        super().__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("User does not exist.")
        if Participant.objects.filter(campaign=self.campaign, user=user).exists():
            raise forms.ValidationError("User is already a participant in this campaign.")
        return user

    def save(self):
        user = User.objects.get(username=self.cleaned_data['username'])
        participant = Participant.objects.create(campaign=self.campaign, user=user, role='player')
        return participant
