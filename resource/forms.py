from django import forms
from django.forms.fields import CharField
from .models import document

class documentforms(forms.ModelForm):
    class Meta:
        model = document
        fields = '__all__'
        labels = {
            "name":"",
            "uploadUser":"",
            "docfile":"",
            "date":"",
            "resourceDesc":"",
            "fileType":"",
            "resourceType":""
        }