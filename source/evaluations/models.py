from django.db import models
from django.contrib.auth.models import User


class Evaluation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    record = models.DecimalField(decimal_places=2, max_digits=3)
    date = models.DateTimeField()

    def __str__(self):
        return self.user.first_name

