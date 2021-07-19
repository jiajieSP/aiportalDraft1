import django_filters
from django.contrib.auth.models import User
from django_filters import DateFilter

class accountFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username','email', 'is_superuser']