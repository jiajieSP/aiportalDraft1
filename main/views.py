from django.http import request
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse, reverse_lazy
from main.models import newsUpdate
from .forms import CreateNewUpdate
from .models import newsUpdate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    a = newsUpdate.objects.order_by('-newsDate')

    p = Paginator(a, 8)
    page = request.GET.get('page')
    a = p.get_page(page)
    return render(request,"main/home.html", {"a":a})

def re_home(response):
    return HttpResponseRedirect('/main/')

def newsCreate(response):
    if response.method == "POST":
        form = CreateNewUpdate(response.POST)
        
        if form.is_valid():
            form.save()
            return redirect("/main/home")
    else:
        form = CreateNewUpdate()
    return render(response, "main/newsCreate.html", {"form":form})
