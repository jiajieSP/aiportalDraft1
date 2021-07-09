from django.contrib import admin
from .models import Item, Search

# Register your models here.
admin.site.register(Search)
admin.site.register(Item)