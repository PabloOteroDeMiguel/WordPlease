# Generated by Django 3.1.3 on 2020-11-05 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogger',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='blogger',
            name='name',
        ),
    ]
