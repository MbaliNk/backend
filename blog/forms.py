from dataclasses import field
from .models import Comment
from django import forms

class Commentforms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')