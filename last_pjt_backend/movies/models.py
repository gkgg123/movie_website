from django.db import models
from django.conf import settings
class Genre(models.Model):
    name = models.CharField(max_length=30)

class Movie(models.Model):
    title = models.CharField(max_length=300)
    original_title = models.CharField(max_length=300)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    adult = models.BooleanField()
    overview = models.TextField()
    original_language = models.CharField(max_length=10)
    poster_path = models.CharField(max_length=100)
    backdrop_path = models.CharField(max_length=100, default='')
    genres = models.ManyToManyField(Genre, related_name='movies')
    def __str__(self):
        return '%s' % (self.title)


class MovieRank(models.Model):
    rank = models.IntegerField(default=0)
    content = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete = models.CASCADE,related_name='movierank')
    created_at = models.DateTimeField(auto_now_add=True)