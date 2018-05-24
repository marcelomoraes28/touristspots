from django.db import models


class TouristSpot(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
