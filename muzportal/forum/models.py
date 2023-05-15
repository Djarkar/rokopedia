from django.db import models
from django.contrib.auth.models import User

class Topics(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название", db_index=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", db_index=True, blank=True)
    category = models.ForeignKey('Categories_post', on_delete=models.CASCADE, verbose_name="Категория", db_index=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering = ['category']

class Posts(models.Model):
    topic = models.ForeignKey('Topics', on_delete=models.CASCADE, verbose_name="Тема", db_index=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", db_index=True, blank=True)
    body = models.TextField(verbose_name="Пост", db_index=True, blank=True)
    post_date = models.DateField(verbose_name="Дата публикации", db_index=True, blank=True)
    category = models.ForeignKey('Categories_post', on_delete=models.CASCADE, verbose_name="Категория", db_index=True, blank=True)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['post_date']

class Posts_img_forum(models.Model):
    post = models.ForeignKey('Posts', on_delete=models.CASCADE, verbose_name="Пост", db_index=True, blank=True)
    img = models.ImageField(upload_to="images/posts", verbose_name="Изображение", db_index=True, blank=True)

    def __str__(self):
        return self.post

    class Meta:
        verbose_name = 'Изображение поста'
        verbose_name_plural = 'Изображения постов'
        ordering = ['post']


class Categories_post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название", db_index=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория поста'
        verbose_name_plural = 'Категории постов'
        ordering = ['title']

class Comments_forum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", db_index=True, blank=True)
    post = models.ForeignKey('Posts', on_delete=models.CASCADE, verbose_name="Пост", db_index=True, blank=True)
    body = models.TextField(verbose_name="Комментарий", db_index=True, blank=True)
    post_date = models.DateField(verbose_name="Дата публикации", db_index=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.post}'

    class Meta:
        verbose_name = 'Комментарий поста'
        verbose_name_plural = 'Комментарии постов'
        ordering = ['post_date']


