from django.contrib import admin
from .models import ProfessionalUser, Posts, MoviesWorked

admin.site.register(ProfessionalUser)
admin.site.register(Posts)
admin.site.register(MoviesWorked)