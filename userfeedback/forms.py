from .models import thread, comment
from django import forms

class createThread(forms.ModelForm):
    class Meta:
        model = thread
        fields = '__all__'

class createComment(forms.ModelForm):
    class Meta:
        model = comment
        fields = '__all__'