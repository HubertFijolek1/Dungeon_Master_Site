from django import forms
from .models import Message, ForumPost, Poll, PollOption
from django.forms.models import inlineformset_factory
from django.contrib.auth import get_user_model

User = get_user_model()

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'content']
        widgets = {
            'receiver': forms.Select(),
            'content': forms.Textarea(attrs={'rows': 4}),
        }

class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['title', 'content', 'campaign']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'campaign']

PollOptionFormSet = inlineformset_factory(
    Poll,
    PollOption,
    fields=('option_text',),
    extra=2,
    can_delete=True
)