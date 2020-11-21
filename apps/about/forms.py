from django import forms
from .models import About

class AboutForm(forms.ModelForm):

    class Meta:
        model = About
        # fields = '__all__'
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs = {'class':'form-control'}),
        }
        labels = {
            'description':''
        }
