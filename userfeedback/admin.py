from django.contrib import admin
from .models import thread, comment

# Register your models here.
admin.site.register(thread)
admin.site.register(comment)