from django.db import models
from django.contrib.postgres.fields import ArrayField

class ProfessionalUser(models.Model):
    name = models.CharField(max_length=512)
    email = models.EmailField()
    password = models.CharField(max_length=512)
    about = models.TextField()
    profile_img = models.TextField(max_length=512, default='')
    experience = models.CharField(max_length = 125)
    location = models.CharField(max_length = 125)
    user_type = models.CharField(max_length=125,  default='')
    movies_worked = ArrayField(
        models.JSONField(blank=True, null=True),
        default=list,
        blank=True,
        null=True
    )
    posts = ArrayField(
        models.JSONField(blank=True, null=True),
        default=list,
        blank=True,
        null=True
    )