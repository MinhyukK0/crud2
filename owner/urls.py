from django.urls import path, re_path
from owner.views import OwnerView, DogView

urlpatterns = [
    path('owner', OwnerView.as_view()),
    path('dog', DogView.as_view()),
]