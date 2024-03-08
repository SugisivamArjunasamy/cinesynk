from django.urls import path
from .views import home_view , profile , studioProfile , login ,guRegister, services, audioservices, vedioservices

urlpatterns = [
    path('', home_view, name='home'),
    path('profile', profile, name='profile'),
    path('studioProfile', studioProfile, name='studioProfile'),
    path('login', login, name='login'),
    path('guRegister', guRegister, name='guRegister'),
    path('services', services, name='services'),
    path('audioservices', audioservices, name='audioservices'),
    path('vedioservices', vedioservices, name='vedioservices'),
]