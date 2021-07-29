from django.contrib import admin
from django.urls import include, path

from . import views

app_name='model'
urlpatterns = [
    path('create', views.createModel, name='create'),
    path('', views.modelList, name='model'),
    path('home', views.re_modelList, name='re_modelList'),
    path('modelResult/<model_id>', views.result, name='modelResult'),
    path('modelSearch', views.modelSearch, name='modelSearch'),
    path('createWER', views.createWER, name='createWER')
]
