from django import forms
from django.forms.fields import CharField
from .models import document

class documentforms(forms.ModelForm):
    name=CharField(max_length=200, label="name")
    class Meta:
        model = document
        fields = ["name", "docfile"]