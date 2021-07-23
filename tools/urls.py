from django.urls import path
from . import views

app_name = 'tools'

urlpatterns = [
    path('', views.home, name='home'),
    path('translate', views.translation, name='translate'),
]