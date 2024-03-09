from django.shortcuts import render
from .serializers import ProfessionalUserSerializer
from .models import ProfessionalUser
# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def profile(request):
    try:
        professional_user = ProfessionalUser.objects.get(email="john@example.com")
        serialized_user = ProfessionalUserSerializer(professional_user)
    except:
        serialized_user = {"user" : "John Doe"}
        
    return render(request, 'profile.html', {"user" : serialized_user.data})

def studioProfile(request):
    return render(request, 'studioProfile.html')
def login(request):
    return render(request, 'login.html')
def guRegister(request):
    return render(request, 'guRegister.html')
def services(request):
    return render(request,'services.html')
def audioservices(request):
    return render(request, 'audiose.html')
def vedioservices(request):
    return render(request,'vediose.html')
def registerop(request):
    return render(request,'registerop.html')
def GeneralRegister(request):
    return render(request, 'guRegister.html')
def directorRegister(request):
    return render(request, 'directorRegister.html')
def studioRegister(request):
    return render(request,'studioRegister.html')