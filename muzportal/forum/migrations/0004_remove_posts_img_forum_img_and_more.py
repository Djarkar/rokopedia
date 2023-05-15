# Generated by Django 4.2 on 2023-05-12 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0003_remove_posts_title_alter_categories_post_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts_img_forum',
            name='img',
        ),
        migrations.AlterField(
            model_name='categories_post',
            name='title',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='comments_forum',
            name='body',
            field=models.TextField(db_index=True),
        ),
        migrations.AlterField(
            model_name='comments_forum',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.posts'),
        ),
        migrations.AlterField(
            model_name='comments_forum',
            name='post_date',
            field=models.DateField(db_index=True),
        ),
        migrations.AlterField(
            model_name='comments_forum',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='posts',
            name='body',
            field=models.TextField(db_index=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.categories_post'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_date',
            field=models.DateField(db_index=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='posts_img_forum',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.posts'),
        ),
        migrations.AlterField(
            model_name='topics',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.categories_post'),
        ),
        migrations.AlterField(
            model_name='topics',
            name='title',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='topics',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
