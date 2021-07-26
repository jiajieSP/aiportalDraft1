from django import forms
from django.forms import widgets
from django.forms.fields import CharField
from .models import document


class documentforms(forms.ModelForm):
    class Meta:
        model = document
        fields = '__all__'
        labels = {
            "name": "",
            "uploadUser": "",
            "docfile": "",
            "date": "",
            "resourceDesc": "",
            "fileType": "",
            "resourceType": ""
        }
        file_choices = (
            ('', '---Select File Type---'),
            ('JPEG', 'JPEG'),
            ('PDF', 'PDF'),
            ('CSV', 'CSV'),
            ('OTHERS', 'OTHERS')
        )
        resource_choices = (
            ('', '---Select Resource Type---'),
            ('USER GUIDE', 'USER GUIDE'),
            ('DATASET', 'DATASET'),
            ('E-BOOK','E-BOOK'),
            ('OTHERS', 'OTHERS')
        )
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Resource Name here'}),
            'uploadUser': forms.TextInput(attrs={'placeholder': 'Enter Name of Uploader'}),
            'resourceDesc': forms.Textarea(attrs={'placeholder': 'Enter Resource Description'}),
            'fileType': forms.Select(choices=file_choices, attrs={'class': 'form-control'}),
            'resourceType': forms.Select(choices=resource_choices, attrs={'class':'form-control'}),
        }
