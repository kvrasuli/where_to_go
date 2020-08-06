from django.db import models

class Place(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.TextField()
    description_long = models.TextField()
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.title