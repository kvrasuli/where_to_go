from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.TextField()
    description_long = HTMLField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        default=None,
        null=True
    )
    image = models.ImageField(upload_to='media/')
    position = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['position']

    def __str__(self):
        return f'{self.id}. {self.title}'
