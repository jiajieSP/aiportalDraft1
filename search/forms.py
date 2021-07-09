from django import forms
from django.forms.fields import DateField
from .models import Search

#Create forms here

class CreateNewModel(forms.ModelForm):
    modelName = forms.CharField(label="", max_length=130, required=True)
    modelText = forms.CharField(label="", max_length=200, required=True)
    modelDate = forms.DateField(label="", required=False)
    modelIntro = forms.CharField(widget=forms.Textarea)
    modelUsage = forms.CharField(widget=forms.Textarea)
    modelStrength = forms.CharField(widget=forms.Textarea)
    modelWeak = forms.CharField(widget=forms.Textarea)
    modelDev = forms.CharField(max_length=200)
    modelDevUnit = forms.CharField(max_length=200)

class CreateForm(forms.ModelForm):
    modelName = forms.CharField(label="", max_length=130, required=True)
    modelText = forms.CharField(label="", max_length=200, required=True)
    modelDate = forms.DateField(label="", required=False)
    modelIntro = forms.CharField(label="",widget=forms.Textarea)
    modelUsage = forms.CharField(label="",widget=forms.Textarea)
    modelStrength = forms.CharField(label="",widget=forms.Textarea)
    modelWeak = forms.CharField(label="",widget=forms.Textarea)
    modelDev = forms.CharField(label="",max_length=200)
    modelDevUnit = forms.CharField(label="",max_length=200)

    class Meta:
        model = Search
        fields = '__all__'

