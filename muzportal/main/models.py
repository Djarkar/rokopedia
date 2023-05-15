from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# NEWS
class Articles(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name="Название", db_index=True)
    body = models.TextField(blank=True, verbose_name="Новость", db_index=True)
    date = models.DateField(max_length=10, blank=True, verbose_name="Дата публикации", db_index=True)
    category = models.ForeignKey('Categories_news', on_delete=models.CASCADE, verbose_name="Категория", db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['date']

class News_img(models.Model):
    article = models.ForeignKey('Articles', on_delete=models.CASCADE, verbose_name="Новость", db_index=True)
    img = models.ImageField(upload_to="images/news", blank=True, verbose_name="Изображение", db_index=True)

    def get_absolute_url(self):
        return reverse('currentnews', kwargs={'id': self.pk})

    def __str__(self):
        return self.article.title

    class Meta:
        verbose_name = 'Изображение новости'
        verbose_name_plural = 'Изображения новостей'
        ordering = ['article']

class Categories_news(models.Model):
    title = models.CharField(max_length=200, blank=True, verbose_name="Название", db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория новости'
        verbose_name_plural = 'Категории новостей'
        ordering = ['title']

class Comments_news(models.Model):
    article = models.ForeignKey('Articles', on_delete=models.CASCADE, verbose_name="Комментарий", db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", db_index=True)
    body = models.TextField(blank=True, verbose_name="Комментарий", db_index=True)
    date = models.DateField(max_length=10, blank=True, verbose_name="Дата", db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['date']


# CONCERTS
class Concerts(models.Model):
    title = models.CharField(max_length=200, blank=True, verbose_name="Название", db_index=True)
    date_of = models.DateField(max_length=10, blank=True, verbose_name="Дата проведения", db_index=True)
    time_of = models.TimeField(max_length=10, blank=True, verbose_name="Время проведения", db_index=True)
    link = models.CharField(max_length=200, blank=True, verbose_name="Ссылка", db_index=True)
    location = models.CharField(max_length=200, blank=True, verbose_name="Место проведения", db_index=True)

    def __str__(self):
        return f'{self.title} - {self.date_of}'

    class Meta:
        verbose_name = 'Концерт'
        verbose_name_plural = 'Концерты'
        ordering = ['date_of']

class Concects_img(models.Model):
    concert = models.ForeignKey('Concerts', on_delete=models.CASCADE, verbose_name="Концерт", db_index=True)
    img = models.ImageField(upload_to="images/concerts",verbose_name="Изображение", db_index=True)

    def __str__(self):
        return self.concert.title

    class Meta:
        verbose_name = 'Изображение концерта'
        verbose_name_plural = 'Изображения концертов'
        ordering = ['id']



# MAIN
class Songs(models.Model):
    title = models.CharField(max_length=200, blank=True, verbose_name="Название", db_index=True)
    artist = models.ForeignKey('Artists', on_delete=models.CASCADE, verbose_name="Исполнитель", db_index=True)
    album = models.ForeignKey('Albums', on_delete=models.CASCADE, verbose_name="Альбом", db_index=True)
    duration = models.TimeField(max_length=6, blank=True, verbose_name="Длительность", db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Музыка'
        verbose_name_plural = 'Музыка'
        ordering = ['title']

class Artists(models.Model):
    name = models.CharField(max_length=200, blank=True, verbose_name="Имя", db_index=True)
    country = models.CharField(max_length=200, blank=True, verbose_name="Страна", db_index=True)
    genre = models.ForeignKey('Genres', on_delete=models.CASCADE, verbose_name="Жанр", db_index=True)
    history = models.TextField(blank=True, verbose_name="История", db_index=True)
    body = models.TextField(blank=True, verbose_name="Описание", db_index=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'
        ordering = ['name']

class Artist_img(models.Model):
    artist = models.ForeignKey('Artists', on_delete=models.CASCADE, verbose_name="Исполнитель", db_index=True)
    img = models.ImageField(upload_to="images/artists", blank=True, verbose_name="Изображение", db_index=True)

    def get_absolute_url(self):
        return reverse('currentartist', kwargs={'id_art': self.pk})

    def __str__(self):
        return self.artist.name

    class Meta:
        verbose_name = 'Изображение исполнителя'
        verbose_name_plural = 'Изображение исполнителей'
        ordering = ['artist']

class Genres(models.Model):
    title = models.CharField(max_length=200, blank=True, verbose_name="Название", db_index=True)

    def __str__(self):
            return self.title

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['title']

class Albums(models.Model):
    title = models.CharField(max_length=200, blank=True, verbose_name="Название", db_index=True)
    artist = models.ForeignKey('Artists', on_delete=models.CASCADE, verbose_name="Исполнитель", db_index=True)
    genre = models.ForeignKey('Genres', on_delete=models.CASCADE, verbose_name="Жанр", db_index=True)
    date_release = models.DateField(max_length=200, blank=True, verbose_name="Дата релиза", db_index=True)
    url_yandex = models.CharField(max_length=200, blank=True, verbose_name="Ссылка на yandex", db_index=True)
    url_vk = models.CharField(max_length=200, blank=True, verbose_name="Ссылка на вк", db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        ordering = ['artist']

class Albums_img(models.Model):
    album = models.ForeignKey('Albums', on_delete=models.CASCADE, verbose_name="Альбом", db_index=True)
    img = models.ImageField(upload_to="images/albums", blank=True, verbose_name="Изображение", db_index=True)

    def get_absolute_url(self):
        return reverse('album', kwargs={'id_album': self.pk})

    def __str__(self):
        return self.album.title

    class Meta:
        verbose_name = 'Изображение альбома'
        verbose_name_plural = 'Изображения альбомов'
        ordering = ['album']

class User_img(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", db_index=True)
    img = models.ImageField(upload_to="images/news", blank=True, verbose_name="Изображение", db_index=True)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'id_user': self.user.pk})

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Изображение пользователя'
        verbose_name_plural = 'Изображение пользователя'
        ordering = ['user']


