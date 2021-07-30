from resource.models import document
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .filters import accountFilter, modelFilter, newsFilter, resourceFilter, threadFilter

from main import models
from main import forms
from main.models import newsUpdate

from register.forms import registerForm
import register

from resource.models import document
from resource.forms import documentforms

from search.models import aiModel, aiModelGraph
from search.forms import CreateForm, createAiForm

from userfeedback import models
from userfeedback.forms import createComment, createThread

#import pagination
from django.core.paginator import Paginator


# Create your views here.
def home(response):
    return render(response,"administration/home.html", {})

def accounts(request):
    User = get_user_model()
    users = User.objects.all()

    filter = accountFilter(request.GET, queryset=users)
    users = filter.qs

    #set up pagination
    p = Paginator(users, 5)
    page = request.GET.get('page')
    m = p.get_page(page)
    
    
    return render(request, "administration/account.html", {'users':users, 'filter':filter, 'm':m})

def updateAccount(request, account_id):
    User = get_user_model()
    users = User.objects.get(pk=account_id)
    form = registerForm(request.POST or None, instance=users)
    if form.is_valid():
        form.save()
        print('form success')
        return redirect('/administration/account')
    else:
        return render (request, 'administration/updateAccount.html', {'users':users, 'form':form})
    
def deleteAccount(request, account_id):
    User = get_user_model()
    users = User.objects.get(pk=account_id)
    users.delete()
    return redirect('/administration/account')

def news(request):
    news = newsUpdate.objects.all()

    filter = newsFilter(request.GET, queryset=news)
    news = filter.qs

    p = Paginator(news, 20)
    page = request.GET.get('page')
    news = p.get_page(page)
    return render(request,"administration/news.html", {'news':news, 'filter':filter})

def updateNews(request, news_id):
    news = newsUpdate.objects.get(pk=news_id)
    form = forms.CreateNewUpdate(request.POST or None, instance=news)
    if form.is_valid():
        form.save()
        print('form success')
        return redirect('/administration/newsList')
    else:
        return render(request, 'administration/updateNews.html', {'news':news,'form':form})

def deleteNews(request, news_id):
    news = newsUpdate.objects.get(pk=news_id)
    news.delete()
    return redirect('/administration/newsList')

def resource(request):
    resource = document.objects.all()

    filter = resourceFilter(request.GET, queryset=resource)
    resource = filter.qs

    p = Paginator(resource, 20)
    page = request.GET.get('page')
    resource = p.get_page(page)

    return render(request, "administration/resource.html", {'resource':resource, 'filter':filter})

def updateResource(request, resource_id):
    resource = document.objects.get(pk=resource_id)
    form = documentforms(request.POST or None, instance=resource)
    if form.is_valid():
        form.save()
        print('form success')
        return redirect('/administration/resourceList')
    else:
        return render(request, 'administration/updateResource.html', {'resource':resource, 'form':form})

def deleteResource(request, resource_id):
    resource = document.objects.get(pk=resource_id)
    resource.delete()
    return redirect('/administration/resourceList')

def model(request):
    model = aiModel.objects.all()
    filter = modelFilter(request.GET, queryset=model)
    model = filter.qs

    p = Paginator(model, 20)
    page = request.GET.get('page')
    model = p.get_page(page)

    return render(request, "administration/model.html", {'model':model, 'filter':filter})

def updateModel(request, model_id):
    model = aiModel.objects.get(pk=model_id)
    form = createAiForm(request.POST or None, instance=model)
    if form.is_valid():
        form.save()
        print('form success')
        return redirect('/administration/modelList')
    else:
        return render(request, 'administration/updateModel.html', {'model':model, 'form':form})

def deleteModel(request, model_id):
    model = aiModel.objects.get(pk=model_id)
    model.delete()
    return redirect('/administration/modelList')

def thread(request):
    thread = models.thread.objects.all()
    filter = threadFilter(request.GET, queryset=thread)
    thread = filter.qs

    p = Paginator(thread, 20)
    page = request.GET.get('page')
    thread = p.get_page(page)

    return render(request, "administration/thread.html", {'thread':thread, 'filter':filter})

def updateThread(request, thread_id):
    thread = models.thread.objects.get(pk=thread_id)
    form = createThread(request.POST or None, instance=thread)
    if form.is_valid():
        form.save()
        print('comments updated')
        return redirect('/administration/threadList')
    else:
        return render(request, 'administration/updateThread.html', {'thread':thread, 'form':form})

def deleteThread(request, thread_id):
    thread = models.thread.objects.get(pk=thread_id)
    thread.delete()
    return redirect('/administration/threadList')