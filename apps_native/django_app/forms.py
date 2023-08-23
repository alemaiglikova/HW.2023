from django import forms
from .models import Idea

class IdeaSubmissionForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ('title', 'description')
