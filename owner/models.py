from django.db import models

# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length= 45)
    email = models.CharField(max_length=300)
    age = models.IntegerField()
    class Meta:
        db_table = 'owners'

class Dog(models.Model):
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    age = models.IntegerField()
    class Meta:
        db_table = 'dogs'

class Actor(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    date_of_birth = models.DateField(default='')
    movie = models.ManyToManyField('Movie')

class Movie(models.Model):
    title = models.CharField()
    release_date = models.DateField(default='')
    runnnig_time = models.IntegerField()
