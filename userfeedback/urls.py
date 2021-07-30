from django.urls import path
from . import views


app_name = 'feedback'

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name='create'),
    path('result/<thread_id>', views.result, name='result'),
    path('comments', views.comments, name='comments')
]