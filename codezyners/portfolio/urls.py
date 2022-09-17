from django.urls import path
from .views import index, ourProjects, reviews, addReview

urlpatterns = [
    path('', index, name="index"),
    path('projects/', ourProjects, name="projects"),
    path('reviews/', reviews, name="reviews"),
    path('add-review/', addReview, name="addReview"),
]
