# Generated by Django 3.2.8 on 2021-10-27 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_restaurant_unique restaurant'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='history',
            options={'verbose_name_plural': 'History'},
        ),
        migrations.AlterModelOptions(
            name='setting',
            options={'verbose_name_plural': 'Settings'},
        ),
    ]