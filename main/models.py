from django.db import models

# Create your models here.
class newsUpdate(models.Model):
    newsName = models.CharField(max_length=200)
    newsDate = models.DateField()
    newsContent = models.CharField(max_length=255)
    newsCreator = models.CharField(max_length=255)

    def __str__(self):
        return self.newsName