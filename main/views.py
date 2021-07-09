from django.http.response import HttpResponseRedirect
from django.urls.base import reverse, reverse_lazy
from main.models import newsUpdate
from .forms import CreateNewUpdate
from django.shortcuts import render, redirect

# Create your views here.
def home(response):
    a = newsUpdate.objects.all()
    return render(response,"main/home.html", {"a":a})

def re_home(response):
    return HttpResponseRedirect('/main/')

