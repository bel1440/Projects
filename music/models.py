from django.db import models

class Singers(models.Model):
    name_singer = models.CharField('Имя исполнителя', max_length=250)
    def __str__(self):
        return self.name_singer

    def get_absolute_url(self):
        return f'/singers/{self.id}'

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

class TypeMusics(models.Model):
    name_type = models.CharField('Жанр', max_length=250)
    description = models.CharField('Описание', max_length=250)
    def __str__(self):
        return self.name_type

    def get_absolute_url(self):
        return f'/genre/{self.id}'

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class Songs(models.Model):
    name_song = models.CharField('Название песни', max_length=250)
    file = models.FileField('Путь', upload_to='')
    def __str__(self):
        return self.name_song

    def get_absolute_url(self):
        return f'/list/{self.id}'

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'

class Users(models.Model):
    name_user = models.CharField('Имя пользователя', max_length=250)
    def __str__(self):
        return self.name_user
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


