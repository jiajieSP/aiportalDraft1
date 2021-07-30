from typing import ContextManager
from django.db import models
from django.utils.translation import TranslatorCommentWarning
import datetime


# Create your models here.
class thread(models.Model):
    title = models.CharField(max_length=130)
    creator = models.CharField(max_length=130, default='test')
    content = models.TextField(blank=True, null=True)
    date = models.DateField(default=datetime.datetime.now)
    ss = models.FileField(upload_to='feedback/', null=True, blank=True)

    def __str__(self):
        return self.title

class comment(models.Model):
    threadTitle = models.ForeignKey(thread, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    date = models.DateTimeField(datetime.datetime.now)
    creator = models.CharField(max_length=130, default='Test')

    def __str__(self):
        return self.content