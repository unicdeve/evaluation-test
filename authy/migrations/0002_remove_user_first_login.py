# Generated by Django 2.2 on 2021-12-10 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_login',
        ),
    ]
