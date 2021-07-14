from django.urls import path
from . import views

app_name='resource'

urlpatterns =[
    path('', views.home, name='resourceHome')
]