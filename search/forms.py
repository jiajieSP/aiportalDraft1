from django import forms
from django.forms.fields import DateField

#Create forms here

class CreateNewModel(forms.Form):
    modelName = forms.CharField(label="modelName", max_length=200, required=True)
    modelText = forms.CharField(label="modelText", max_length=200, required=True)
    modelDate = forms.DateField(label="modelDate", required=False)