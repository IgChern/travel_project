# Generated by Django 4.2.7 on 2024-03-23 21:13

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users_app', '0001_initial'),
        ('trip_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=3000, verbose_name='Comment')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Time_create')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Time_update')),
                ('status', models.CharField(choices=[('published', 'Опубликован'), ('deleted', 'Удален')], default='published', max_length=9)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_author', to='users_app.user')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='social_app.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='trip_app.post')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ['-time_create'],
            },
        ),
        migrations.CreateModel(
            name='CommentRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(choices=[(1, 'Upvote'), (-1, 'Downvote')], verbose_name='Value')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_ratings', to='users_app.user')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='trip_app.post')),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Ratings',
                'ordering': ('-time_create',),
                'indexes': [models.Index(fields=['-time_create', 'value'], name='social_app__time_cr_4f163a_idx')],
                'unique_together': {('post', 'author')},
            },
        ),
    ]
