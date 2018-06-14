from django.db import models


class Attraction(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    initial_period = models.TextField()
    minimum_age = models.IntegerField()
    photo = models.ImageField(upload_to="attraction", null=True, blank=True)

    def __str__(self):
        return self.name
