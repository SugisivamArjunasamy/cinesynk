from django.urls import path
from .views import get_professional_user

urlpatterns=[
    path("prouser/", get_professional_user, name="prouser")
]