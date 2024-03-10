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
        
    def create(self, validated_data):
        validated_data['movies_worked'] = []
        validated_data['posts'] = []
        return super().create(validated_data)
    
class ProfessionalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalUser
        fields = ['id', 'name', 'email', 'password', 'about', 'profile_img', 'experience', 'location', 'user_type', 'movies_worked', 'posts']

class MoviesWorked(serializers.Serializer):
    thumbnail = serializers.CharField()
    email = serializers.EmailField()
    title = serializers.CharField()
    description = serializers.CharField()

class PostsSerializer(serializers.Serializer):
    thumbnail = serializers.CharField()
    email = serializers.EmailField()
    type = serializers.ChoiceField(choices=["image", "video"])
    description = serializers.CharField()