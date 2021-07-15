from django.urls import path
from . import views

app_name='resource'

urlpatterns =[
    path('', views.home, name='resourceHome'),
    path('upload', views.upload, name='resourceUpload'),
    path('resourceSearch', views.resourceSearch, name='resourceSearch'),
    path('resourceResult/<resource_id>', views.resourceResult, name='resourceResult'),
]