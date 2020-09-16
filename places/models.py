from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description_short = models.TextField(verbose_name='Краткое описание')
    description_long = HTMLField(verbose_name='Подробное описание')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        verbose_name='Название',
        related_name='images'
    )
    image = models.ImageField(upload_to='media/', verbose_name='Изображение')
    position = models.PositiveIntegerField(
        default=0, blank=False, null=False,
        verbose_name='Позиция в списке'
    )

    class Meta(object):
        ordering = ['position']

    def __str__(self):
        return f'{self.id}. {self.title}'
