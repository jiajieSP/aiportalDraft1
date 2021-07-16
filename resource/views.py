from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from .models import document
from .forms import documentforms

# Create your views here.

def resourceResult(response, resource_id):
    m = document.objects.get(pk = resource_id)
    return render(response, "resource/resourceResult.html", {"m":m})

def home(response):
    documents = document.objects.all()
    return render(response, "resource/home.html", {"documents":documents})

def upload(request):
    message = "Upload any file"
    if request.method == "POST":
        print('method is post')
        form = documentforms(request.POST, request.FILES)
        print('form variable filled')
        print(form)
        if form.is_valid():
            form.save()
            print("form saved")
            return  HttpResponseRedirect("/resource/")
        else:
            message = "form not successful"
    else:
        form = documentforms()

    context = {
        'form': form,
        'message': message
    }
    return render(request, "resource/upload.html", context)

def resourceSearch(response):
    if response.method == "POST":
        searched = response.POST['searched']
        m = document.objects.filter(name__contains=searched)
        
        return render(response, "resource/searchResult.html", {'searched':searched, 'm':m})
    else:
        return render(response, "resource/searchResult.html", {})


