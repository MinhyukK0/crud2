from django.urls import path, re_path
from owner.views import OwnerView, DogView

urlpatterns = [
    re_path('owner', OwnerView.as_view()),
    re_path('dog', DogView.as_view()),
]