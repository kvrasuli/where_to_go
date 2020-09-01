from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.TextField()
    description_long = models.TextField()
    lat = models.DecimalField(max_digits=9, decimal_places=3)
    lng = models.DecimalField(max_digits=9, decimal_places=3)

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.ForeignKey(
        Place,
        on_delete=models.DO_NOTHING,
        default=None,
        null=True
    )
    image = models.ImageField(upload_to='media/')
    position = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['position']

    def __str__(self):
        return f'{self.id}. {self.title}'
