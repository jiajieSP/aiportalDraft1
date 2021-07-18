# Generated by Django 3.2.5 on 2021-07-15 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0001_initial_manual'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='fileType',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='resourceDesc',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='document',
            name='resourceType',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='uploadUser',
            field=models.CharField(max_length=50, null=True),
        ),
    ]