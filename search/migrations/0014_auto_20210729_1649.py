# Generated by Django 3.2.5 on 2021-07-29 08:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0013_auto_20210729_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aimodel',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='aimodelgraph',
            name='recordDate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
