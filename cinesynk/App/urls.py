from django.urls import path
from .views import home_view, profile, login ,guRegister, services, audioservices, vedioservices
from .views import registerop ,register_view , post, chat_view

urlpatterns = [
    path('', home_view, name='home'),
    path('profile', profile, name='profile'),
    path('login', login, name='login'),
    path('guRegister', guRegister, name='guRegister'),
    path('services', services, name='services'),
    path('audioservices', audioservices, name='audioservices'),
    path('vedioservices', vedioservices, name='vedioservices'),
    path('registerop', registerop, name='registerop'),
    path('register', register_view, name='register'),
    path('post', post, name='post'),
    path("chat", chat_view, name='chat')
]