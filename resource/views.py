from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from .models import document
from .forms import documentforms

# Create your views here.


def home(request):
    message = "Upload any file"
    if request.method == "POST":
        print('method is post')
        form = documentforms(request.POST, request.FILES)
        print('form variable filled')
        if form.is_valid():
            newdoc = document(docfile=request.FILES['docfile'])
            print("form referenced")
            newdoc.save()
            print("form saved")

            return  HttpResponseRedirect("/resource/")
        else:
            message = "form not successful"
            print(form._errors)
    else:
        form = documentforms()

    documents = document.objects.all()

    context = {
        'documents': documents,
        'form': form,
        'message': message
    }
    return render(request, "resource/home.html", context)
