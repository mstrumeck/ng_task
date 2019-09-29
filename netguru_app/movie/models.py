from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=30)
    year = models.IntegerField()
    rated = models.CharField(max_length=5)
    released = models.TextField()
    runtime = models.TextField()
    genre = models.TextField()
    director = models.TextField()
    writer = models.TextField()
    actors = models.TextField()
    plot = models.TextField()
    language = models.TextField()
    country = models.TextField()
    awards = models.TextField()
    imdb_id = models.TextField()
