# Generated by Django 3.2.5 on 2021-07-26 02:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_newsupdate_newscontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsupdate',
            name='newsDate',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
