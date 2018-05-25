from django.db import models
from attractions.models import Attraction
from comments.models import Comment
from evaluations.models import Evaluation


class TouristSpot(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    approved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attraction)
    comments = models.ManyToManyField(Comment)
    evaluations = models.ManyToManyField(Evaluation)

    def __str__(self):
        return self.name
