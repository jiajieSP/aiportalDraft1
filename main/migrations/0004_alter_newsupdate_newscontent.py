# Generated by Django 3.2.5 on 2021-07-22 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_creator_newsupdate_newscreator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsupdate',
            name='newsContent',
            field=models.TextField(),
        ),
    ]
