# Generated by Django 4.2 on 2023-05-16 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_comments_forum_post_date_alter_posts_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments_forum',
            name='body',
            field=models.CharField(blank=True, db_index=True, max_length=1000, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='comments_forum',
            name='post_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
    ]
