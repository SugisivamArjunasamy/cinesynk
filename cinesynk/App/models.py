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

    def __str__(self):
        return self.name
    
class Posts(models.Model):
    posted_by = models.ForeignKey(ProfessionalUser, on_delete=models.CASCADE)
    source = models.TextField(max_length=512, default='')
    post_type = models.TextField(max_length=512, default='')
    description = models.TextField(max_length=512, default='')
    posted_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.posted_by} : {self.posted_time}"

class MoviesWorked(models.Model):
    worked_by = models.ForeignKey(ProfessionalUser, on_delete=models.CASCADE)
    thumbnail = models.TextField(max_length=512, default='')
    title = models.CharField(max_length=125, default='')
    description = models.TextField(max_length=512, default='')
    added_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} : {self.worked_by}"
    
class Service(models.Model):
    title = models.CharField(max_length=125, default='')
    posted_by = models.ForeignKey(ProfessionalUser, on_delete=models.CASCADE)
    thumbnail = models.TextField(max_length=512, default='')
    description = models.TextField(max_length=512, default='')
    added_time = models.DateTimeField(auto_now_add=True)
    service_type = models.TextField(max_length=512, default='')

    def __str__(self):
        return f"{self.title} by {self.posted_by}"