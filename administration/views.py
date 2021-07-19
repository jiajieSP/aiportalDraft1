from register.forms import registerForm
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
import register
from .filters import accountFilter

# Create your views here.
def home(response):
    return render(response,"administration/home.html", {})

def accounts(request):
    User = get_user_model()
    users = User.objects.all()
    filter = accountFilter(request.GET, queryset=users)
    users = filter.qs
    return render(request, "administration/account.html", {'users':users, 'filter':filter})

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