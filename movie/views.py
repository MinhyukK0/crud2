from django.db.models.query import Prefetch
from django.shortcuts import render

# Create your views here.

import json
from django.http import JsonResponse
from django.views import View
from movie.models import Movie, Actor
from django.utils import timezone

# Actors
class ActorView(View):
    # get
    def get(self, request): 
        results = []
        actors = Actor.objects.prefetch_related('movie').all()
        for actor in actors:
            results.append(
                {
                    '이름'  : actor.first_name,
                    '성'   : actor.last_name,
                    '생일'  : actor.date_of_birth,
                    '출연영화': [x.title for x in actor.movie.all()],
                }
            )
        return JsonResponse({'results' : results}, status = 200)
    # post
    def post(self, request):
        data = json.loads(request.body)
        Actor.objects.create(
            first_name = data['이름'],
            last_name = data['성'],
            date_of_birth = data['생일'],
        )
        return JsonResponse({'MESSAGE':'Created'},status = 201)

# Movie
class MovieView(View):
    # get
    def get(self, request): 
        results = []
        movies = Movie.objects.prefetch_related('actor_set').all()
        for movie in movies:
            results.append(
                {
                    'title'       : movie.title,
                    'release_date': movie.release_date,
                    'running_time': movie.running_time,
                    'actor'       : [x.first_name for x in movie.actor_set.all()],
                }
            )
        return JsonResponse({'results' : results}, status = 200)
    # post
    def post(self, request):
        data = json.loads(request.body)
        Movie.objects.create(
            title = data['제목'],
            release_date = data['개봉날짜'],
            running_time = data['상영시간'],
        )
        return JsonResponse({'MESSAGE':'Created'},status = 201)