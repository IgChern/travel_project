# Generated by Django 4.2.7 on 2024-03-23 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trips',
            name='slug',
            field=models.SlugField(default='', max_length=255, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', max_length=255, verbose_name='URL'),
        ),
    ]
