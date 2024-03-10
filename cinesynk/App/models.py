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
    user_type = models.TextField(max_length=512, default='')

class Posts(models.Model):
    posted_by = models.ForeignKey(ProfessionalUser, on_delete=models.CASCADE)
    source = models.TextField(max_length=512, default='')
    post_type = models.TextField(max_length=512, default='')
    description = models.TextField(max_length=512, default='')
    posted_time = models.DateTimeField()

class MoviesWorked(models.Model):
    worked_by = models.ForeignKey(ProfessionalUser, on_delete=models.CASCADE)
    thumbnail = models.TextField(max_length=512, default='')
    title = models.CharField(max_length=125, default='')
    description = models.TextField(max_length=512, default='')
    added_time = models.DateTimeField()