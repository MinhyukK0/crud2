from typing import AsyncGenerator
from django.urls import path, re_path
from movie.views import MovieView, ActorView


urlpatterns = [
    path('actor', ActorView.as_view()),
    path('movie', MovieView.as_view()),
]