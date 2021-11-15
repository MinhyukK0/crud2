from django.db import models

# Create your models here.
from datetime import datetime
from django.utils import timezone

class Actor(models.Model):
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    date_of_birth = models.DateTimeField()
    movie = models.ManyToManyField('Movie')
    
    class Meta():
        db_table = 'actors'

class Movie(models.Model):
    title = models.CharField(max_length= 50)
    release_date = models.DateTimeField()
    running_time = models.IntegerField()
    
    class Meta():
        db_table = 'movies'