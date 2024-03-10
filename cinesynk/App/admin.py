from django.contrib import admin
from .models import ProfessionalUser, Posts, MoviesWorked, Service, Message

admin.site.register(ProfessionalUser)
admin.site.register(Posts)
admin.site.register(MoviesWorked)
admin.site.register(Service)
admin.site.register(Message)