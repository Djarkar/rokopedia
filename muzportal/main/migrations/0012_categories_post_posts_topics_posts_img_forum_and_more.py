# Generated by Django 4.2 on 2023-05-15 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0011_delete_user_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=200, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория поста',
                'verbose_name_plural': 'Категории постов',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, db_index=True, verbose_name='Пост')),
                ('post_date', models.DateField(blank=True, db_index=True, verbose_name='Дата публикации')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.categories_post', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['post_date'],
            },
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=200, verbose_name='Название')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.categories_post', verbose_name='Категория')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
                'ordering': ['category'],
            },
        ),
        migrations.CreateModel(
            name='Posts_img_forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, db_index=True, upload_to='images/posts', verbose_name='Изображение')),
                ('post', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.posts', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Изображение поста',
                'verbose_name_plural': 'Изображения постов',
                'ordering': ['post'],
            },
        ),
        migrations.AddField(
            model_name='posts',
            name='topic',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.topics', verbose_name='Тема'),
        ),
        migrations.AddField(
            model_name='posts',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.CreateModel(
            name='Comments_forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, db_index=True, verbose_name='Комментарий')),
                ('post_date', models.DateField(blank=True, db_index=True, verbose_name='Дата публикации')),
                ('post', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.posts', verbose_name='Пост')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Комментарий поста',
                'verbose_name_plural': 'Комментарии постов',
                'ordering': ['post_date'],
            },
        ),
    ]