from django.shortcuts import redirect, render
from .forms import translate
from googletrans import Translator
# Create your views here.

def home(response):
    return render(response, 'tools/home.html', {})

def translation(request):
    form = translate(request.POST)
    if form.is_valid():
        name = form.cleaned_data['text']
        translator = Translator()
        tr = translator.translate(name)
        return render(request, 'tools/translator.html', {'form':form, 'name':name, 'tr':tr})
    else:
        form = translate()
        return render(request, 'tools/translator.html', {'form':form})