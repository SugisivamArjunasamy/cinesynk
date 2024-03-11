from django.shortcuts import render
from .serializers import ProfessionalUserSerializer
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import LoginForm, SearchForm, RegistrationForm, MessageForm, EnquireForm
from .models import ProfessionalUser, MoviesWorked, Posts, Service, Message
from django.db.models import Q

def home_view(request):
    user_token = request.session.get('user_token')
    profile_img = request.session.get('profile_img')
    if user_token:
        return render(request, "home.html", {"profile_img" : profile_img})
    else:
        return HttpResponseRedirect(reverse('login'))

def profile(request):
    user_email = request.GET.get('email')
    if user_email:
        user_token = user_email
        user_type ='studio'

    else:
        user_token = request.session.get('user_token')
        user_type = request.session.get('user_type')

    profile_img = request.session.get('profile_img')
    
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
    
    if request.method == "POST":
    
        form = SearchForm(request.POST)
        
        if form.is_valid():
            search_query = form.cleaned_data.get('searchInput')
            provided_services = Service.objects.filter(service_type="audio", title__icontains=search_query, ).order_by('-added_time')
            return render(request,'audiose.html', {"profile_img" : profile_img, "services" : provided_services})

    else:
        
        if not user_token:
            return HttpResponseRedirect(reverse('login'))
        
        try:
            provided_services = Service.objects.all().filter(service_type="audio").order_by('-added_time')
            
        except Service.DoesNotExist:
                provided_services = []
                
        return render(request,'audiose.html', {"profile_img" : profile_img, "services" : provided_services})

def vedioservices(request):
    user_token = request.session.get('user_token')
    profile_img = request.session.get('profile_img')
    if request.method == "POST":

        form = SearchForm(request.POST)
        
        if form.is_valid():
            search_query = form.cleaned_data.get('searchInput')
            provided_services = Service.objects.filter(service_type="video", title__icontains=search_query).order_by('-added_time')
            return render(request,'vediose.html', {"profile_img" : profile_img, "services" : provided_services})

    else:
        if not user_token:
            return HttpResponseRedirect(reverse('login'))
        
        try:
            provided_services = Service.objects.all().filter(service_type="video").order_by('-added_time')
            
        except Service.DoesNotExist:
                provided_services = []
                
        return render(request,'vediose.html', {"profile_img" : profile_img, "services" : provided_services})

def registerop(request):
    return render(request,'registerop.html')

def register_view(request):
    user_type = request.GET.get('type')
    if not user_type:
        return HttpResponseRedirect(reverse('registerop'))

    if request.method == "POST":
        form = RegistrationForm(request.POST)

        
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            confirmpassword = form.cleaned_data.get('confirmpassword')

            if password != confirmpassword:
                return render(request, 'register.html', {"form": form, "error_message": "Passwords doesn't Match."})
            try:
                user = ProfessionalUser.objects.get(email=email)
                return render(request, 'register.html', {"form": form, "error_message": "Email alreay registered"})
            except ProfessionalUser.DoesNotExist:
                ProfessionalUser.objects
                return
        else:
            return render(request, 'login.html', {"form": form})
        return render(request, 'register.html', {'user_type': user_type})
        
    else:

        return render(request, 'register.html', {'user_type': user_type})


def post(request):
    user_token = request.session.get('user_token')
    profile_img = request.session.get('profile_img')
    
    if not user_token:
        return HttpResponseRedirect(reverse('login'))
    
    posts = posts = Posts.objects.order_by('-posted_time')
    return render(request, 'post.html', {"profile_img" : profile_img, "posts" : posts})

def chat_view(request):
    user_email = request.session.get('user_token')
    profile_img = request.session.get('profile_img')
    
    if request.method == "POST":
        form = MessageForm(request.POST)
        
        if form.is_valid():
            message = form.cleaned_data.get('message')
            recipient_email = form.cleaned_data.get('recipient_email')
            
            sender = ProfessionalUser.objects.get(email=user_email)
            recipient = ProfessionalUser.objects.get(email=recipient_email)
            new_message = Message(sender=sender, recipient=recipient, content=message)
            new_message.save()
            return HttpResponseRedirect(reverse('chat'))
        
    else:
        messages = Message.objects.filter(Q(sender__email=user_email) | Q(recipient__email=user_email)).order_by('timestamp')
        conversations = {}

        for message in messages:

            if message.sender.email != user_email and message.sender.email not in conversations:
                conversations[message.sender.email] = {
                    'name': message.sender.name,
                    'profile_img': message.sender.profile_img,
                    "user_type" : message.sender.user_type,
                    'email' : message.sender.email,


                }
            
            elif message.recipient.email != user_email and message.recipient.email not in conversations:
                conversations[message.recipient.email] = {
                    'name': message.recipient.name,
                    'email' : message.recipient.email,
                    'profile_img': message.recipient.profile_img,
                    "user_type" : message.recipient.user_type 
                }

        unique_users = list(conversations.values())
        if len(unique_users) > 0:
            recipient_email = unique_users[0]['email']
        else:
            recipient_email = ""
        return render(request, "chat.html", {"profile_img" : profile_img, "messages" : messages, "current_user" :user_email, "conversations" : unique_users,  'recipient_email' : recipient_email})


def enquire_view(request):
    user_email = request.session.get('user_token')
    profile_img = request.session.get('profile_img')

    if request.method == "POST":
        form = EnquireForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get('title')
            service_email = form.cleaned_data.get('service_email')
            description = form.cleaned_data.get('description')
            
            sender = ProfessionalUser.objects.get(email=user_email)
            recipient = ProfessionalUser.objects.get(email=service_email)
            message = f"Hello {recipient.name}, I am interested in your {title} Service. Can you send me the further details"
            new_message = Message(sender=sender, recipient=recipient, content=message)
            new_message.save()
        
    return HttpResponseRedirect(reverse('chat'))