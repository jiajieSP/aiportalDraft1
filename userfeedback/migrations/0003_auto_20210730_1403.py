# Generated by Django 3.2.5 on 2021-07-30 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userfeedback', '0002_alter_thread_ss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='threadTitle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='userfeedback.thread'),
        ),
    ]