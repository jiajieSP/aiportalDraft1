from django.db import models
from django.db.models.fields import TextField

# Create your models here.
class document(models.Model):
    name = models.CharField(max_length=200, null=True)
    docfile = models.FileField(upload_to='documents/')
    date = models.DateField(blank=True, null=True)
    uploadUser = models.CharField(max_length=50, null=True)
    resourceType = models.CharField(max_length=200, null=True)
    fileType = models.CharField(max_length=200, null=True)
    resourceDesc = models.TextField(blank=True)

    def __str__(self):
        return self.name