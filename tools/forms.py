from django import forms
from django.forms.widgets import Textarea

class translate(forms.Form):
    text = forms.CharField(widget=Textarea, label='')
