# Generated by Django 3.2.8 on 2021-10-23 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='summary',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='summary',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='vote_amount',
            field=models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=5, null=True),
        ),
    ]
