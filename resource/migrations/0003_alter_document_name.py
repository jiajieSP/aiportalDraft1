# Generated by Django 3.2.5 on 2021-07-15 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0002_auto_20210715_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='name',
            field=models.CharField(default='admin', max_length=200),
        ),
    ]
