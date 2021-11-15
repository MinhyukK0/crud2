from django.db import models

# Create your models here.

class Actor(models.Model):
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    date_of_birth = models.DateField(default='')
    movie = models.ManyToManyField('Movie')
    
    class Meta():
        db_table = 'actors'

class Movie(models.Model):
    title = models.CharField(max_length= 50)
    release_date = models.DateField(default='')
    runnnig_time = models.IntegerField()
    
    class Meta():
        db_table = 'movies'