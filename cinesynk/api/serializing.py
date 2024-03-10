from rest_framework import serializers
from App.models import ProfessionalUser

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

class UpdateFieldSerializer(serializers.Serializer):
    field_name = serializers.CharField()
    field_value = serializers.CharField()
    email = serializers.EmailField()

class CreateProfessionalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalUser
        fields = [ 'name', 'email', 'password', 'about', 'profile_img', 'experience', 'location', 'user_type']
    
class ProfessionalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalUser
        fields = ['id', 'name', 'email', 'password', 'about', 'profile_img', 'experience', 'location', 'user_type']
