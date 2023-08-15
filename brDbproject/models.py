from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class CastCrew(models.Model):
    role = models.CharField(max_length=20, choices=(('Director', 'Director'), ('Actor', 'Actor'), ('Writer', 'Writer')))
    name = models.CharField(max_length=50)
    biography = models.TextField(max_length=10000)
    castcrewURL = models.URLField(max_length=500)
    def __str__(self):
        return self.name + " as " + self.role 

class Movies(models.Model):
    title = models.CharField(max_length=100, error_messages={
            'required': 'my required msg..',
        })
    summary = models.TextField(max_length=10000)
    year = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )
    duration = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )
    imdb_r = models.FloatField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ])
    country = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    movieURL = models.URLField(max_length=500)
    coverURL = models.URLField(max_length=500)

    castcrews = models.ManyToManyField(CastCrew)
    def __str__(self):
        return self.title

class Reviews(models.Model):
    username = models.CharField(max_length=20)
    rating = models.IntegerField()
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=10000)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
