# Generated by Django 3.0.6 on 2020-05-15 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panaderia',
            name='redirectTo',
        ),
    ]
