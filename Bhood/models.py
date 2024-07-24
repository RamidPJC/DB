from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    cont = models.TextField(verbose_name='Содержание')
    category = models.ManyToManyField('Cate', blank=True, verbose_name='Категории')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Изображение')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Cate(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    category = models.ManyToManyField(Post, blank=True, verbose_name='Связанные посты')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Messenger(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    message = models.CharField(max_length=500, verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
    def __str__(self):
        return f'{self.author} {self.message}'

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    profile_pic = models.ImageField(upload_to='photos_of_profile/%Y/%m/%d/', blank=True, default='default.jpg', verbose_name='Аватарка')
    def __str__(self):
        return self.name.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

class Predlozka(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    cont = models.TextField(verbose_name='Содержание')
    category = models.ManyToManyField('Cate', blank=True, verbose_name='Категории')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Изображение')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Предложенные записи'

class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    comment = models.CharField(max_length=500, verbose_name='Комментарий')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Связанный пост')
    def __str__(self):
        return f'{self.author} : {self.comment}'
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class RatePost(models.Model):
    rate = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')), verbose_name='Оценка')
    rate_count = models.IntegerField(null=True, blank=True, default=1, verbose_name='Кол-во оценок')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Связанный пост')
    person = models.ForeignKey(Profile, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Оценивший')
    def __str__(self):
        return f'{self.post.title} : {self.rate}'
    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'