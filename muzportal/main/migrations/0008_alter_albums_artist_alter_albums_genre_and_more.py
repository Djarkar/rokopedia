# Generated by Django 4.2 on 2023-05-12 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_alter_albums_img_img_alter_artist_img_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albums',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.artists', verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='albums',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.genres', verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='albums_img',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.albums', verbose_name='Альбом'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.categories_news', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='artist_img',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.artists', verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='artists',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.genres', verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='comments_news',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.articles', verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='comments_news',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='concects_img',
            name='concert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.concerts', verbose_name='Концерт'),
        ),
        migrations.AlterField(
            model_name='news_img',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.articles', verbose_name='Новость'),
        ),
        migrations.AlterField(
            model_name='songs',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.albums', verbose_name='Альбом'),
        ),
        migrations.AlterField(
            model_name='songs',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.artists', verbose_name='Исполнитель'),
        ),
    ]
