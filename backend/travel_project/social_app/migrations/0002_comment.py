# Generated by Django 4.0 on 2024-03-18 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trip_app', '0001_initial'),
        ('users_app', '0001_initial'),
        ('social_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=3000, verbose_name='Comment')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Time_create')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Time_update')),
                ('status', models.CharField(choices=[('published', 'Опубликовано'), ('draft', 'Черновик')], default='published', max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_author', to='users_app.user')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='trip_app.post')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['-time_create'],
            },
        ),
    ]
