from django.db import models

# Create your models here.
class document(models.Model):
    name = models.CharField(max_length=200, null=True)
    docfile = models.FileField(upload_to='documents/')