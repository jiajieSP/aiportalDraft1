from django.db import models
from datetime import date
from django.db.models.fields import CharField, IntegerField
from django.utils.timezone import now
import datetime

# Create your models here.

# class SearchList(models.Model):
#     modelName = models.CharField(max_length=200)
#     modelText = models.CharField(max_length=255,unique=True, null=True)
#     modelDate = models.DateField(blank=True, null=True)


#     def __str__(self):
#         return (self.modelName, self.modelText, self.modelDate)

class Search(models.Model):
    modelName = models.CharField(verbose_name='Model Name' ,max_length=130)
    modelText = models.CharField(max_length=50,unique=True, null=True)
    modelDate = models.DateField(default=datetime.datetime.now)
    modelIntro = models.TextField(blank=True,null=True)
    modelUsage = models.TextField(blank=True,null=True)
    modelStrength = models.TextField(blank=True,null=True)
    modelWeak = models.TextField(blank=True,null=True)
    modelDev = models.CharField(max_length=200,unique=False, null=True)
    modelDevUnit = models.CharField(max_length=200,unique=False, null=True)

    def __str__(self):
        return '%s %s %s'%(self.modelName, self.modelText, self.modelDate)

class Item(models.Model):
    desc = models.CharField(max_length=255)

    def __str__(self):
        return self.desc

class aiModel(models.Model):
    name = models.CharField(verbose_name='Name of Model',max_length=130)
    date = models.DateField(default=datetime.date.today)
    usage = models.TextField(blank=True,null=True)
    creator = models.CharField(max_length=130,blank=True,null=True)

    def __str__(self):
        return self.name
    
class aiModelGraph(models.Model):
    modelName = models.ForeignKey(aiModel, on_delete=models.CASCADE)
    recordName = models.CharField(verbose_name='Name of Record', max_length=130)
    recordDate = models.DateField(default=datetime.date.today)
    recordWer = models.IntegerField(blank=False, default='0')
    recordWordcount = models.IntegerField(blank=False, default='0')
        
    def __str__(self):
        return self.modelName