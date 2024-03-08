from rest_framework import serializers
from App.models import ProfessionalUser

class GetProffesionalUserSerializer(serializers.Serializer):
    email = serializers.EmailField()

class ProfessionalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalUser
        fields = ['id', 'name', 'email', 'password', 'about', 'profile_img', 'experience', 'location', 'user_type', 'movies_worked', 'posts']