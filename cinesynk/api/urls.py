from django.urls import path
from .views import get_professional_user, update_professional_user, create_professional_user

urlpatterns=[
    path("prouser", get_professional_user, name="prouser"),
    path("prouser/update", update_professional_user, name="updateProuser"),
    path("prouser/create",  create_professional_user, name="createprouser"),
]