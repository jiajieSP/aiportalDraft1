# Generated by Django 3.2.5 on 2021-07-09 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='modelDev',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='modelIntro',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='modelStrength',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='modelUsage',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='modelWeak',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
