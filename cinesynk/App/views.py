from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'home.html')
def profile(request):
    return render(request, 'profile.html')
def studioProfile(request):
    return render(request, 'studioProfile.html')
def login(request):
    return render(request, 'login.html')