# Generated by Django 3.2.8 on 2021-10-27 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='restaurant',
            constraint=models.UniqueConstraint(fields=('name',), name='unique restaurant'),
        ),
    ]
