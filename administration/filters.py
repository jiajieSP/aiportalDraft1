
import django_filters
from django.contrib.auth.models import User
from django_filters import DateFilter

from main.models import newsUpdate
from resource.models import document
from search.models import Search

class accountFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username','email', 'is_superuser']

class newsFilter(django_filters.FilterSet):
    class Meta:
        model = newsUpdate
        fields = ['newsName', 'newsDate', 'newsCreator']

class resourceFilter(django_filters.FilterSet):
    class Meta:
        model = document
        fields = ['name', 'date', 'resourceType', 'resourceDesc', 'uploadUser']

class modelFilter(django_filters.FilterSet):
    class Meta:
        model = Search
        fields = ['modelName', 'modelText','modelDate', 'modelDev', 'modelDevUnit']