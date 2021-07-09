from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Search
from .forms import CreateForm, CreateNewModel
from django.urls import reverse, reverse_lazy

# Create your views here.
# def SearchIndex(response, id):
#     s = Search.objects.get(id=id)
#     # return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(s.modelName, i.desc))
#     # model = Search.objects.get(id=id)
#     return render(response,"search/result.html", {"model":s})

def result(response, model_id):
    m = Search.objects.get(pk = model_id)
    return render(response,"search/result.html", {"m":m})


def createModel(response):
    if response.method == "POST":
        form = CreateForm(response.POST)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect("/search/")
    else:
        form = CreateForm()
    return render(response,"search/createModel.html", {"form":form})


def modelList(response):
    m = Search.objects.all()
    return render(response, "search/modelList.html", {"m":m})

def re_modelList(response):
    return HttpResponseRedirect('/search/')

def modelSearch(response):
    if response.method == "POST":
        searched = response.POST['searched']
        m = Search.objects.filter(modelName__contains=searched)
        return render(response, "search/searchResults.html", {'searched':searched, 'm':m})
    else:
        return render(response, "search/searchResults.html", {})


# def searchResults(response):
#     if response.method == "POST":
#         searched = response.POST['searched']
#         m = Search.objects.filter(name__contains=searched)
#         return render(response,'search/searchResults.html', {'searched':searched, 'm':models})
#     else:
#         return render(response,'search/searchResults.html', {})