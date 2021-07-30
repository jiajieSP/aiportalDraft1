# Generated by Django 3.2.5 on 2021-07-30 04:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='thread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=130)),
                ('content', models.TextField(blank=True, null=True)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('ss', models.FileField(null=True, upload_to='feedback/')),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('threadTitle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userfeedback.thread')),
            ],
        ),
    ]