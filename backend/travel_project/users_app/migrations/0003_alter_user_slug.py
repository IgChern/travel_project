# Generated by Django 4.2.7 on 2024-03-23 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0002_user_comments_count_user_votes_down_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(default='', max_length=255, verbose_name='URL'),
        ),
    ]
