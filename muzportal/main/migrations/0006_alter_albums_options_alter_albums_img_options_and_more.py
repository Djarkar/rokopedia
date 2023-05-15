# Generated by Django 4.2 on 2023-05-12 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_albums_options_alter_albums_img_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='albums',
            options={'ordering': ['artist'], 'verbose_name': 'Альбом', 'verbose_name_plural': 'Альбомы'},
        ),
        migrations.AlterModelOptions(
            name='albums_img',
            options={'ordering': ['album'], 'verbose_name': 'Изображение альбома', 'verbose_name_plural': 'Изображения альбомов'},
        ),
        migrations.AlterModelOptions(
            name='articles',
            options={'ordering': ['date'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterModelOptions(
            name='artist_img',
            options={'ordering': ['artist'], 'verbose_name': 'Изображение исполнителя', 'verbose_name_plural': 'Изображение исполнителей'},
        ),
        migrations.AlterModelOptions(
            name='artists',
            options={'ordering': ['name'], 'verbose_name': 'Исполнитель', 'verbose_name_plural': 'Исполнители'},
        ),
        migrations.AlterModelOptions(
            name='categories_news',
            options={'ordering': ['title'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='comments_news',
            options={'ordering': ['date'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='concects_img',
            options={'ordering': ['id'], 'verbose_name': 'Изображение концерта', 'verbose_name_plural': 'Изображения концертов'},
        ),
        migrations.AlterModelOptions(
            name='concerts',
            options={'ordering': ['date_of'], 'verbose_name': 'Концерт', 'verbose_name_plural': 'Концерты'},
        ),
        migrations.AlterModelOptions(
            name='genres',
            options={'ordering': ['title'], 'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='news_img',
            options={'ordering': ['article'], 'verbose_name': 'Изображение новости', 'verbose_name_plural': 'Изображения новостей'},
        ),
        migrations.AlterModelOptions(
            name='songs',
            options={'ordering': ['title'], 'verbose_name': 'Музыка', 'verbose_name_plural': 'Музыка'},
        ),
    ]