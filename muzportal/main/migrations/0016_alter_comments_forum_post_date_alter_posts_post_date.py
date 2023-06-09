# Generated by Django 4.2 on 2023-05-16 07:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_comments_forum_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments_forum',
            name='post_date',
            field=models.DateField(blank=True, db_index=True, default=datetime.datetime(2023, 5, 16, 12, 22, 9, 887444), verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_date',
            field=models.DateField(blank=True, db_index=True, default=datetime.datetime(2023, 5, 16, 12, 22, 9, 886126), verbose_name='Дата публикации'),
        ),
    ]
