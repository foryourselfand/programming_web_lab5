from django.contrib.auth.models import User
from django.db import models


class Dot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    x = models.IntegerField()
    y = models.FloatField()
    r = models.IntegerField()
    result = models.BooleanField()

    def __str__(self):
        return f'x={self.x}; y={self.y}; r={self.r}; user={self.user}'
