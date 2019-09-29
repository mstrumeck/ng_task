from django.db import models
from django.utils import timezone

from movie.models import Movie


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created = models.DateField(default=timezone.now())
    text = models.TextField()
