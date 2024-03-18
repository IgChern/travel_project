# Generated by Django 4.0 on 2024-03-18 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users_app', '0002_alter_user_options_user_bio_alter_user_avatar_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255, verbose_name='Location')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('start_date', models.DateTimeField(verbose_name='Start_date')),
                ('end_date', models.DateTimeField(verbose_name='End_date')),
                ('photo', models.URLField(blank=True, verbose_name='Photo')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_trip', to='users_app.user')),
            ],
            options={
                'verbose_name': 'Trip',
                'verbose_name_plural': 'Trips',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=255, verbose_name='URL')),
                ('status', models.CharField(choices=[('published', 'Опубликовано'), ('draft', 'Черновик')], default='published', max_length=10, verbose_name='status')),
                ('place_name', models.CharField(max_length=255, verbose_name='Place_name')),
                ('place_type', models.CharField(blank=True, max_length=255, verbose_name='Place_type')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('photo', models.URLField(blank=True, verbose_name='Photo')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Date_create')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Date_update')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='author_posts', to='users_app.user')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_trip', to='trip_app.trips')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
