from django import forms
from .models import Message, ForumPost
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