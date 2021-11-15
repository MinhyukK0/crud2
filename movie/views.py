from django.shortcuts import render

# Create your views here.

import json
from django.http import JsonResponse
from django.views import View
from movie.models import Movie, Actor

# Actors
class ActorView(View):
    # post 
    def post(self, request): 
        data = json.loads(request.body)
        Actor.objects.create(
            first_name    = data['first_name'],
            last_name     = data['last_name'],
            date_of_birth = data['date_of birth'],
            )
        return JsonResponse({'MESSAGE' : 'Created'}, status = 201)
    # get
    def get(self, request): 
        results = []
        actors = Actor.objects.all()
        for actor in actors:
            results.append(
                {
                    'first_name'   : actor.first_name,
                    'last_name'    : actor.last_name,
                    'date_of_birth': actor.date_of_birth,
                    'movie'        : actor.movie.name
                }
            )
        return JsonResponse({'results' : results}, status = 200)

# Movie
class MovieView(View):
    # post 
    def post(self, request): 
        data = json.loads(request.body)
        Actor.objects.create(
            title        = data['title'],
            release_date = data['release_date'],
            running_time = data['running_time'],
        )
        return JsonResponse({'MESSAGE' : 'Created'}, status = 201)
    # get
    def get(self, request): 
        results = []
        movies = Movie.objects.all()
        for movie in movies:
            results.append(
                {
                    'title'       : movie.title,
                    'release_date': movie.release_date,
                    'running_time': movie.ruunning_time,
                    'actor'       : [x.first_name for x in movie.actor_set.all()]
                }
            )
        return JsonResponse({'results' : results}, status = 200)