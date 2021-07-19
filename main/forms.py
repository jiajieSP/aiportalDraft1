from administration.views import news
from django import forms
from django.forms.fields import DateField
from .models import newsUpdate

# Create forms here


class CreateNewUpdate(forms.ModelForm):
    class Meta:
        model = newsUpdate
        fields = '__all__'

