from django.urls import path
from .views import get_professional_user, update_professional_user, create_professional_user, add_movie_worked, add_post

urlpatterns=[
    path("prouser", get_professional_user, name="prouser"),
    path("prouser/update", update_professional_user, name="updateProuser"),
    path("prouser/create",  create_professional_user, name="createprouser"),
    path("prouser/movies/add", add_movie_worked, name="addmovies"),
    path("prouser/posts/add", add_post, name="addposts")
]