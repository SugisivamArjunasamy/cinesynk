from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializing import GetProffesionalUserSerializer, ProfessionalUserSerializer
from App.models import ProfessionalUser

@api_view(['GET'])
def get_professional_user(request):
    serializer = GetProffesionalUserSerializer(data=request.query_params)

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