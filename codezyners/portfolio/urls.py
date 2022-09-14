from django.urls import path
from .views import index, ourProjects, about, quota, reviews, addReview

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('projects/', ourProjects, name="projects"),
    path('quota/', quota, name="quota"),
    path('reviews/', reviews, name="reviews"),
    path('add-review/', addReview, name="addReview"),
]
