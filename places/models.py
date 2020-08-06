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
    image = models.ImageField(upload_to='media/')
    # title = models.CharField(max_length=255)

    # def __str__(self):
    #     return self.title

