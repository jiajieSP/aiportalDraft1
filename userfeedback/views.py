from django.core import paginator
from django.shortcuts import redirect, render
from .forms import createComment, createThread
from .models import thread
from django.core.paginator import Paginator

# Create your views here.
def home (request):
    m = thread.objects.order_by('-date')
    
    p=Paginator(m, 15)
    page = request.GET.get('page')
    m = p.get_page(page)
    return render(request, 'userfeedback/home.html', {'m':m})

def create(request):
    form = createThread(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        print('thread created')
        return redirect('/feedback')
    else:
        form = createThread()
        return render(request, 'userfeedback/create.html', {'form':form})

def result(request, thread_id):
    m = thread.objects.get(pk = thread_id)
    return render(request, 'userfeedback/thread.html', {'m':m})

def comments(request):
    form = createComment(request.POST)
    if form.is_valid():
        form.save()
        print('comment created')
        return redirect('/feedback')
    else:
        form = createComment()
        return render(request, 'userfeedback/comments.html', {'form':form})