# Generated by Django 3.2.8 on 2021-10-26 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0009_settings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Settings',
            new_name='Setting',
        ),
    ]
