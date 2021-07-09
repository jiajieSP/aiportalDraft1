from django import forms
from django.forms.fields import DateField

# Create forms here


class CreateNewUpdate(forms.Form):
    newsName = forms.CharField(label="newsName", max_length=200)
    newsDate = forms.DateField()
    newsContent = forms.CharField(label="newsContent", max_length=200)
    newsCreator = forms.CharField(label="newsCreator", max_length=200)
