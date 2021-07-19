from django.urls import path

from . import views
import register

app_name = 'devs'

urlpatterns = [
    path('', views.home, name='home'),
    path('register', register.views.register, name='register'),
    path('account', views.accounts, name='account'),
    path('updateAccount/<account_id>', views.updateAccount, name='updateAccount'),
    path('deleteAccount/<account_id>', views.deleteAccount, name='deleteAccount'),
]