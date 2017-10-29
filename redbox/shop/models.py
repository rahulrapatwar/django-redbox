from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    genre = models.CharField(max_length=250)
    rating = models.PositiveIntegerField()
    image = models.ImageField(upload_to='game_pics',blank=True)

    def __str__(self):
        return self.title

class Movie(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    genre = models.CharField(max_length=250)
    rating = models.PositiveIntegerField()
    image = models.ImageField(upload_to='movie_pics',blank=True)

    def __str__(self):
        return self.title
