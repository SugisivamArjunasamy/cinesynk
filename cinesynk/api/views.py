from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializing import EmailSerializer, ProfessionalUserSerializer, UpdateFieldSerializer, CreateProfessionalUserSerializer
from App.models import ProfessionalUser

@api_view(['GET'])
def get_professional_user(request):

    serializer = EmailSerializer(data=request.data)

    if serializer.is_valid():
        email = serializer.validated_data['email']
        try:
            professional_user = ProfessionalUser.objects.get(email=email)
            serialized_user = ProfessionalUserSerializer(professional_user)

            return Response(serialized_user.data)
        
        except ProfessionalUser.DoesNotExist:
            return Response("Professional user does not exist", status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def update_professional_user(request):
    serializer = UpdateFieldSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        field_name = serializer.validated_data['field_name']
        field_value = serializer.validated_data['field_value']
        try:
            professional_user = ProfessionalUser.objects.get(email=email)
            if hasattr(professional_user, field_name):
                setattr(professional_user, field_name, field_value)
                professional_user.save()
                return Response(f"{field_name} updated successfully")
            else:
                return Response(f"Field '{field_name}' does not exist in the ProfessionalUser model", status=status.HTTP_400_BAD_REQUEST)
        
        except ProfessionalUser.DoesNotExist:
            return Response("Professional user does not exist", status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def create_professional_user(request):
    serializer = CreateProfessionalUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Professional user created successfully", status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)