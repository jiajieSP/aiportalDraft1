# Generated by Django 3.2.5 on 2021-07-29 03:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0011_aimodel_creator'),
    ]

    operations = [
        migrations.CreateModel(
            name='aiModelGraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recordName', models.CharField(max_length=130, verbose_name='Name of Record')),
                ('recordDate', models.DateField(default=datetime.datetime.now)),
                ('recordWer', models.IntegerField(default='0')),
                ('recordWordcount', models.IntegerField(default='0')),
                ('modelName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.aimodel')),
            ],
        ),
    ]
