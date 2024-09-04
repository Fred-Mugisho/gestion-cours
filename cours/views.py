from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *

# Create your views here.

def home(request):
    nom = "toto"
    context = {
        'nom': nom
    }
    return render(request, 'cours/home.html', context)

def login_system(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        users = User.objects.filter(email=email)
        if users.exists():
            user = users.first()
            
            user_auth = authenticate(
                request, 
                username=user.username, 
                password=password
            )
            if user_auth:
                login(request, user_auth)
                
                return redirect('cours:dashboard')
            else:
                messages.error(request, 'Email et/ou mot de passe incorrect')
                return redirect('cours:login')
        else:
            messages.error(request, 'Email et/ou mot de passe incorrect')
            return redirect('cours:login')
    
    return render(request, 'cours/login.html')

def register(request):
    if request.method == 'POST':
        nom_complet = request.POST.get('nom_complet')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # nom_cours = request.POST.get('nom_cours')
        
        users = User.objects.filter(email=email)
        if users.exists():
            messages.error(request, 'Un compte avec cette adresse email existe déja')
            return redirect('cours:register')
        else:
            # cours = Cours(
            #     nom=nom_cours,
            #     description="Description du cours",
            # )
            # cours.save()
            user = User(
                username=nom_complet,
                email=email,
            )
            user.set_password(password)
            user.save()
            
            messages.success(request, 'Compte crée avec succès')
            return redirect('cours:login')
        
    return render(request, 'cours/register.html')

def dashboard(request):
    return render(request, 'cours/dashboard.html')