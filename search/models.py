from django.db import models
from datetime import datetime
from django.db.models.fields import CharField
from django.utils.timezone import now

# Create your models here.

# class SearchList(models.Model):
#     modelName = models.CharField(max_length=200)
#     modelText = models.CharField(max_length=255,unique=True, null=True)
#     modelDate = models.DateField(blank=True, null=True)


#     def __str__(self):
#         return (self.modelName, self.modelText, self.modelDate)

class Search(models.Model):
    modelName = models.CharField(max_length=200)
    modelText = models.CharField(max_length=255,unique=True, null=True)
    modelDate = models.DateField(blank=True, null=True)


    def __str__(self):
        return '%s %s %s'%(self.modelName, self.modelText, self.modelDate)

class Item(models.Model):
    search = models.ForeignKey(Search, on_delete=models.CASCADE)
    desc = models.CharField(max_length=255)

    def __str__(self):
        return self.desc