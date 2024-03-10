from django.shortcuts import render
from .serializers import ProfessionalUserSerializer
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import LoginForm
from .models import ProfessionalUser, MoviesWorked, Posts, Service

def home_view(request):
    user_token = request.session.get('user_token')
    profile_img = request.session.get('profile_img')
    if user_token:
        return render(request, "home.html", {"profile_img" : profile_img})
    else:
        return HttpResponseRedirect(reverse('login'))

def profile(request):
    user_token = request.session.get('user_token')
    profile_img = request.session.get('profile_img')
    user_type = request.session.get('user_type')
    
    if not user_token:
        return HttpResponseRedirect(reverse('login'))
    
    try:
        professional_user = ProfessionalUser.objects.get(email=user_token)
        serialized_user = ProfessionalUserSerializer(professional_user)
    except:
        serialized_user = {"user" : "John Doe"}
    
    userData = serialized_user.data
    try:
        movies_worked = MoviesWorked.objects.filter(worked_by=professional_user).order_by('-added_time')
    except MoviesWorked.DoesNotExist:
        movies_worked = []
    userData['movies_worked'] = movies_worked

    try:
        posts = Posts.objects.filter(posted_by=professional_user).order_by('-posted_time')
    except Posts.DoesNotExist:
        posts = []
    userData['posts'] = posts

    if user_type == "professional":
        return render(request, 'profile.html', {"user" : userData,"profile_img" : profile_img})
    
    elif user_type == "studio":
        try:
            provided_services = Service.objects.filter(posted_by=professional_user).order_by('-added_time')
        
        except Service.DoesNotExist:
            provided_services = []
        
        userData['services'] = provided_services
        return render(request, 'studioProfile.html', {"user" : userData,"profile_img" : profile_img})
    
    else:
        return HttpResponseRedirect(reverse('login'))

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = ProfessionalUser.objects.get(email=email)
            except ProfessionalUser.DoesNotExist:
                return render(request, 'login.html', {"form": form, "error_message": "Invalid email or password."})

            if password== user.password:
                request.session['user_token'] = user.email
                request.session['profile_img'] = user.profile_img
                request.session['user_type'] = user.user_type

                return HttpResponseRedirect(reverse('home'))
            else:
                return render(request, 'login.html', {"form": form, "error_message": "Invalid email or password."})
        
        else:
            return render(request, 'login.html', {"form": form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {"form": form})

def guRegister(request):
    return render(request, 'guRegister.html')

def services(request):
    user_token = request.session.get('user_token')
    profile_img = request.session.get('profile_img')

    if not user_token:
        return HttpResponseRedirect(reverse('login'))
    return render(request,'services.html', {"profile_img" : profile_img})

def audioservices(request):
    user_token = request.session.get('user_token')
    profile_img = request.session.get('profile_img')
    
    if not user_token:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'audiose.html', {"profile_img" : profile_img})

def vedioservices(request):
    user_token = request.session.get('user_token')
    profile_img = request.session.get('profile_img')
    
    if not user_token:
        return HttpResponseRedirect(reverse('login'))
    return render(request,'vediose.html', {"profile_img" : profile_img})

def registerop(request):
    return render(request,'registerop.html')

def GeneralRegister(request):
    return render(request, 'guRegister.html')

def directorRegister(request):
    return render(request, 'directorRegister.html')

def studioRegister(request):
    return render(request,'studioRegister.html')

def post(request):
    user_token = request.session.get('user_token')
    profile_img = request.session.get('profile_img')
    
    if not user_token:
        return HttpResponseRedirect(reverse('login'))
    
    posts = posts = Posts.objects.order_by('-posted_time')
    return render(request, 'post.html', {"profile_img" : profile_img, "posts" : posts})