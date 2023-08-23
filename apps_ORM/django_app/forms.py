from django import forms
from .models import UsefulIdea

class UsefulIdeaForm(forms.ModelForm):
    class Meta:
        model = UsefulIdea
        fields = ['title', 'description', 'submitted_by']
