from django.forms import widgets
from administration.views import news
from django import forms
from django.forms.fields import DateField
from .models import newsUpdate

# Create forms here


class CreateNewUpdate(forms.ModelForm):
    class Meta:
        model = newsUpdate
        fields = '__all__'
        labels = {
            'newsName':'',
            'newsDate':'',
            'newsCreator':'',
            'newsContent':''
        }
        widgets = {
            'newsName': forms.TextInput(attrs={'placeholder': 'Enter News Name here'}),
            'newsCreator': forms.TextInput(attrs={'placeholder': 'Enter News Creator here'}),
            'newsContent': forms.Textarea(attrs={'placeholder': 'Enter News Content here'}),
        }

