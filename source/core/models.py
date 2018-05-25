from django.db import models
from attractions.models import Attraction


class TouristSpot(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    approved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attraction)

    def __str__(self):
        return self.name
