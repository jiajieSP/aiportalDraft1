
from os import name
from typing import Text
from django.forms import widgets
from django.forms.widgets import DateInput, TextInput, Widget
import django_filters
from django.contrib.auth.models import User
from django_filters import DateFilter
from django_filters.filters import ChoiceFilter

from main.models import newsUpdate
from resource.models import document
from resource.forms import documentforms
from search.models import Search, aiModel


class accountFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(label='Name', widget=TextInput(attrs={'placeholder':'Enter User Name'}))
    email = django_filters.CharFilter(label='Name', widget=TextInput(attrs={'placeholder':'Enter Email'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'is_superuser']


class newsFilter(django_filters.FilterSet):
    newsName = django_filters.CharFilter(label='Name of News', widget=TextInput(attrs={'placeholder':'News Name'}))
    newsDate = django_filters.DateFilter(label='Enter Date Here', widget=DateInput(attrs={'placeholder':'YYYY-MM-DD'}))
    newsCreator = django_filters.CharFilter(label='Name of Creator', widget=TextInput(attrs={'placeholder':'Creator Name'}))
    class Meta:
        model = newsUpdate
        fields = ['newsName', 'newsDate', 'newsCreator']

file_choices = (
    ('JPEG', 'JPEG'),
    ('PDF', 'PDF'),
    ('CSV', 'CSV'),
    ('EPUB', 'EPUB'),
    ('OTHERS', 'OTHERS')
)
resource_choices = (
    ('USER GUIDE', 'USER GUIDE'),
    ('DATASET', 'DATASET'),
    ('E-BOOK', 'E-BOOK'),
    ('OTHERS', 'OTHERS')
)


class resourceFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Name of Resource', widget=TextInput(attrs={'placeholder':'Resource Name'}))
    fileType = django_filters.ChoiceFilter(choices = file_choices, label='Select File Type')
    resourceType = django_filters.ChoiceFilter(choices = resource_choices, label='Select Resource Type')
    uploadUser = django_filters.CharFilter(label='Name of Uploader', widget=TextInput(attrs={'placeholder':'Uploader Name'}))
    date = django_filters.DateFilter(label='Enter Date Here', widget=DateInput(attrs={'placeholder':'YYYY-MM-DD'}))
    class Meta:
        model = document
        fields = ['name', 'date', 'resourceType', 'fileType', 'uploadUser']

class modelFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Name of Resource', widget=TextInput(attrs={'placeholder':'Model Name'}))
    date = django_filters.DateFilter(label='Enter Date Here', widget=DateInput(attrs={'placeholder':'YYYY-MM-DD'}))
    creator = django_filters.CharFilter(label='Name of Uploader', widget=TextInput(attrs={'placeholder':'Uploader Name'}))
    class Meta:
        model = aiModel
        fields = ['name', 'date', 'creator']
