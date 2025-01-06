from .models import Comment
from about.models import CollaborateRequest as Collaborate
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class CollaborateForm(forms.ModelForm):
    class Meta:
        model = Collaborate
        fields = ('name', 'email', 'message',)
