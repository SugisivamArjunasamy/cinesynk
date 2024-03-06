from django.urls import path
from .views import home_view , profile , studioProfile

urlpatterns = [
    path('', home_view, name='home'),
    path('profile', profile, name='profile'),
    path('studioProfile', studioProfile, name='studioProfile'),
]