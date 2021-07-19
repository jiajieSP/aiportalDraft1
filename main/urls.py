from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.re_home, name='re_home'),

]