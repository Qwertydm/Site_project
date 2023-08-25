from django.db import models

# Create your models here.
class Novosti(models.Model):
    title_nv = models.CharField('Название', max_length=50)
    anons_nv = models.CharField('Анонс', max_length=250)
    full_text_nv = models.TextField('Статья')
    date_nv = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title_nv

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
