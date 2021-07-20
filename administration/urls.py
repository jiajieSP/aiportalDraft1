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
    path('newsList', views.news, name='newsList'),
    path('updateNews/<news_id>', views.updateNews, name='updateNews'),
    path('deleteNews/<news_id>', views.deleteNews, name='deleteNews'),
    path('resourceList', views.resource, name='resourceList'),
    path('updateResource/<resource_id>', views.updateResource, name='updateResource'),
    path('deleteResource/<resource_id>', views.deleteResource, name='deleteResource'),
    path('modelList', views.model, name='modelList'),
    path('updateModel/<model_id>', views.updateModel, name='updateModel'),
    path('deleteModel/<model_id>', views.deleteModel, name='deleteModel')
]