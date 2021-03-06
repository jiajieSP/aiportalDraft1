from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from .models import document
from .forms import documentforms
from django.core.paginator import Paginator

# Create your views here.

def resourceResult(response, resource_id):
    m = document.objects.get(pk = resource_id)
    return render(response, "resource/resourceResult.html", {"m":m})

def home(request):
    documents = document.objects.order_by('-date')

    p = Paginator(documents, 15)
    page = request.GET.get('page')
    documents = p.get_page(page)

    return render(request, "resource/home.html", {"documents":documents})

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

def resourceSearch(request):
    if request.method == "POST":
        searched = request.POST['searched']
        m = document.objects.filter(name__contains=searched)

        p = Paginator(m, 75)
        page = request.GET.get('page')
        m = p.get_page(page)
        
        return render(request, "resource/searchResult.html", {'searched':searched, 'm':m})
    else:
        return render(request, "resource/searchResult.html", {})


