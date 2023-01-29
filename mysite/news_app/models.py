from django.conf import settings
from django.db import models
from django.urls import reverse
from django.core import validators


class Category(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('categories', kwargs={'categories_name': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class News(models.Model):
    title = models.CharField(max_length=120,verbose_name='Заголовок', validators=[validators.MinLengthValidator(12)])
    content = models.TextField(verbose_name='Контент', validators=[validators.MinLengthValidator(25)])
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_name': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Comment(models.Model):
    news = models.ForeignKey('News', on_delete=models.CASCADE, verbose_name='Новость')
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Имя пользователя')
    content = models.TextField(max_length=255, verbose_name='Текст комментария')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']