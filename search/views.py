from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.utils.html import urlize
from matplotlib.pyplot import xcorr
from .models import  aiModel, aiModelGraph
from .forms import CreateForm, CreateNewModel, createAiForm, createAiGraphForm
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from .utils import get_plot

# Create your views here.
# def SearchIndex(response, id):
#     s = Search.objects.get(id=id)
#     # return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(s.modelName, i.desc))
#     # model = Search.objects.get(id=id)
#     return render(response,"search/result.html", {"model":s})

def result(response, model_id):
    m = aiModel.objects.get(pk = model_id)
    i = aiModelGraph.objects.filter(modelName=model_id)
    y = [y.recordWer for y in i]
    x = [x.recordDate for x in i]
    chart = get_plot(x,y)
    print('here is x')
    print(x)
    print(y)
    return render(response,"search/result.html", {"m":m, 'chart':chart})


def createWER(request):
    if request.method == "POST":
        form = createAiGraphForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/search')
        else:
            print('not successful')
    else:
        form = createAiGraphForm()
    return render(request, 'search/uploadWER.html', {'form':form})

def createModel(request):
    if request.method == "POST":
        form = createAiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/search')
        else:
            print('not successful')
    else:
        form = createAiForm()
    return render(request,"search/createModel.html", {"form":form})


def modelList(request):
    m = aiModel.objects.order_by('-date')

    p = Paginator(m, 15)
    page = request.GET.get('page')
    m = p.get_page(page)

    return render(request, "search/modelList.html", {"m":m})

def re_modelList(response):
    return HttpResponseRedirect('/search/')

def modelSearch(request):
    if request.method == "POST":
        searched = request.POST['searched']
        m = aiModel.objects.filter(name__contains=searched)

        p = Paginator(m, 75)
        page = request.GET.get('page')
        m = p.get_page(page)
        
        return render(request, "search/searchResults.html", {'searched':searched, 'm':m})
    else:
        return render(request, "search/searchResults.html", {})


# def searchResults(response):
#     if response.method == "POST":
#         searched = response.POST['searched']
#         m = Search.objects.filter(name__contains=searched)
#         return render(response,'search/searchResults.html', {'searched':searched, 'm':models})
#     else:
#         return render(response,'search/searchResults.html', {})