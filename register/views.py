from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import registerForm
from django.http.response import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            print('form success')

        return redirect("/administration/account")
    else:
        form = UserCreationForm()
    return render(response, "register/register.html", {"form": form})
