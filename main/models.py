from django.db import models
import datetime

# Create your models here.
class newsUpdate(models.Model):
    newsName = models.CharField(max_length=200)
    newsDate = models.DateField(default=datetime.datetime.now)
    newsContent = models.TextField()
    newsCreator = models.CharField(max_length=255)

    def __str__(self):
        return self.newsName