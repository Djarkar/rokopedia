# Generated by Django 4.2 on 2023-05-12 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_alter_albums_date_release_alter_articles_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'ordering': ['id'], 'verbose_name': ('Новость',), 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='albums',
            name='artist',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.artists', verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='albums',
            name='date_release',
            field=models.DateField(blank=True, max_length=200, verbose_name='Дата релиза'),
        ),
        migrations.AlterField(
            model_name='albums',
            name='genre',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.genres', verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='albums',
            name='title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='albums',
            name='url_vk',
            field=models.CharField(blank=True, max_length=200, verbose_name='Ссылка на вк'),
        ),
        migrations.AlterField(
            model_name='albums',
            name='url_yandex',
            field=models.CharField(blank=True, max_length=200, verbose_name='Ссылка на yandex'),
        ),
        migrations.AlterField(
            model_name='albums_img',
            name='album',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.albums', verbose_name='Альбом'),
        ),
        migrations.AlterField(
            model_name='albums_img',
            name='img',
            field=models.CharField(blank=True, max_length=200, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='body',
            field=models.TextField(blank=True, verbose_name='Новость'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.categories_news', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateField(blank=True, max_length=10, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='artist_img',
            name='artist',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.artists', verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='artist_img',
            name='img',
            field=models.CharField(blank=True, max_length=200, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='artists',
            name='body',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='artists',
            name='country',
            field=models.CharField(blank=True, max_length=200, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='artists',
            name='genre',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.genres', verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='artists',
            name='history',
            field=models.TextField(blank=True, verbose_name='История'),
        ),
        migrations.AlterField(
            model_name='artists',
            name='name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='categories_news',
            name='title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='comments_news',
            name='article',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.articles', verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='comments_news',
            name='body',
            field=models.TextField(blank=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='comments_news',
            name='date',
            field=models.DateField(blank=True, max_length=10, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='comments_news',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='concects_img',
            name='concert',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.concerts', verbose_name='Концерт'),
        ),
        migrations.AlterField(
            model_name='concects_img',
            name='img',
            field=models.ImageField(upload_to='images/concerts', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='concerts',
            name='date_of',
            field=models.DateField(blank=True, max_length=10, verbose_name='Дата проведения'),
        ),
        migrations.AlterField(
            model_name='concerts',
            name='link',
            field=models.CharField(blank=True, max_length=200, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='concerts',
            name='location',
            field=models.CharField(blank=True, max_length=200, verbose_name='Место проведения'),
        ),
        migrations.AlterField(
            model_name='concerts',
            name='time_of',
            field=models.TimeField(blank=True, max_length=10, verbose_name='Время проведения'),
        ),
        migrations.AlterField(
            model_name='concerts',
            name='title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='genres',
            name='title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='news_img',
            name='article',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.articles', verbose_name='Новость'),
        ),
        migrations.AlterField(
            model_name='news_img',
            name='img',
            field=models.ImageField(blank=True, upload_to='images/news', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='songs',
            name='album',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.albums', verbose_name='Альбом'),
        ),
        migrations.AlterField(
            model_name='songs',
            name='artist',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.artists', verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='songs',
            name='duration',
            field=models.TimeField(blank=True, max_length=6, verbose_name='Длительность'),
        ),
        migrations.AlterField(
            model_name='songs',
            name='title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='songs',
            name='url_vk',
            field=models.CharField(blank=True, max_length=200, verbose_name='Ссылка на вк'),
        ),
        migrations.AlterField(
            model_name='songs',
            name='url_yandex',
            field=models.CharField(blank=True, max_length=200, verbose_name='Ссылка на yandex'),
        ),
    ]
