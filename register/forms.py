from django import forms
from django.contrib.auth import load_backend, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class registerForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = "username", "email", "password1", "password2"
        labels = {"username": "", "email": "",
                  "password1": "", "password2": ""}
