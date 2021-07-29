from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.fields import DateField
from django.forms.models import model_to_dict
from django.forms.widgets import SelectDateWidget
from .models import Search, aiModel, aiModelGraph

# Create forms here


class CreateNewModel(forms.ModelForm):
    modelName = forms.CharField(label="", max_length=130, required=True)
    modelText = forms.CharField(label="", max_length=200, required=True)
    modelDate = forms.DateField(label="", widget=SelectDateWidget)
    modelIntro = forms.CharField(widget=forms.Textarea)
    modelUsage = forms.CharField(widget=forms.Textarea)
    modelStrength = forms.CharField(widget=forms.Textarea)
    modelWeak = forms.CharField(widget=forms.Textarea)
    modelDev = forms.CharField(max_length=200)
    modelDevUnit = forms.CharField(max_length=200)


class CreateForm(forms.ModelForm):
    # modelName = forms.CharField(label="", max_length=130, required=True)
    # modelText = forms.CharField(label="", max_length=200, required=True)
    # modelDate = forms.DateField(label="", widget=SelectDateWidget)
    # modelIntro = forms.CharField(label="",widget=forms.Textarea)
    # modelUsage = forms.CharField(label="",widget=forms.Textarea)
    # modelStrength = forms.CharField(label="",widget=forms.Textarea)
    # modelWeak = forms.CharField(label="",widget=forms.Textarea)
    # modelDev = forms.CharField(label="",max_length=200)
    # modelDevUnit = forms.CharField(label="",max_length=200)

    class Meta:
        model = Search
        fields = '__all__'

##Final 
class createAiForm(forms.ModelForm):
    class Meta:
        model = aiModel
        fields = '__all__'
        labels = {
            "name": "",
            "date": "",
            "usage": "",
            "creator": "",
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Model Name here'}),
            'creator': forms.TextInput(attrs={'placeholder': 'Enter Model Creator here'}),
            'usage': forms.Textarea(attrs={'placeholder': 'Enter Model Usage Description'}),
        }

class createAiGraphForm(forms.ModelForm):
    class Meta:
        model = aiModelGraph
        fields = '__all__'
        labels = {}
        choices_model = (
            aiModel.name, aiModel.name
        )
        widgets = {
            'modelName': forms.Select(choices=choices_model, attrs={'class': 'form-control'})
        }