from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *

# Vue de la page d'accueil
def home(request):
    # Cette vue affiche simplement la page d'accueil du site web.
    return render(request, 'cours/home.html')

# Vue pour la gestion de la connexion
def login_system(request):
    # Si la requête est de type POST (soumission du formulaire de connexion)
    if request.method == 'POST':
        # Récupération des données du formulaire
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Recherche de l'utilisateur correspondant à l'email fourni
        users = User.objects.filter(email=email)
        if users.exists():  # Si l'utilisateur existe
            user = users.first()
            
            # Authentification de l'utilisateur avec son nom d'utilisateur et son mot de passe
            user_auth = authenticate(
                request, 
                username=user.username, 
                password=password
            )
            if user_auth:  # Si l'authentification est réussie
                # Connexion de l'utilisateur et redirection vers la page "mes cours"
                login(request, user_auth)
                return redirect('cours:mes_cours')
            else:
                # Affichage d'un message d'erreur si les informations sont incorrectes
                messages.error(request, 'Email et/ou mot de passe incorrect')
                return redirect('cours:login')
        else:
            # Affichage d'un message d'erreur si l'email n'est pas reconnu
            messages.error(request, 'Email et/ou mot de passe incorrect')
            return redirect('cours:login')
    
    # Si la requête est de type GET, on affiche la page de connexion
    return render(request, 'cours/login.html')

# Vue pour l'inscription d'un nouvel utilisateur
def register(request):
    # Si la requête est de type POST (soumission du formulaire d'inscription)
    if request.method == 'POST':
        # Récupération des données du formulaire
        nom_complet = request.POST.get('nom_complet')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Vérification de l'existence d'un compte avec cet email
        users = User.objects.filter(email=email)
        if users.exists():  # Si un compte existe déjà avec cet email
            messages.error(request, 'Un compte avec cette adresse email existe déjà')
            return redirect('cours:register')
        else:  # Création d'un nouveau compte utilisateur
            user = User(
                username=nom_complet,
                email=email,
            )
            user.set_password(password)  # Définition du mot de passe de l'utilisateur
            user.save()  # Sauvegarde du compte utilisateur dans la base de données
            
            messages.success(request, 'Compte créé avec succès')
            return redirect('cours:login')
        
    # Si la requête est de type GET, on affiche la page d'inscription
    return render(request, 'cours/register.html')

# Vue pour l'affichage des cours de l'utilisateur connecté
@login_required  # Cette vue nécessite que l'utilisateur soit connecté
def mes_cours(request):
    # Récupération des cours de l'enseignant connecté et tri par nom
    cours = Cours.objects.filter(enseignant=request.user).order_by('nom')
    context = {
        'cours': cours  # Les cours sont passés au contexte pour être affichés dans le template
    }
    return render(request, 'cours/mes_cours.html', context)

# Vue pour ajouter un nouveau cours
@login_required
def add_cours(request):
    # Si la requête est de type POST (soumission du formulaire d'ajout de cours)
    if request.method == 'POST':
        cours_form = CoursForm(request.POST)
        if cours_form.is_valid():
            cours = cours_form.save(commit=False)  # On ne sauvegarde pas encore le cours
            cours.enseignant = request.user  # On assigne l'enseignant connecté au cours
            cours.save()  # Sauvegarde du cours
            messages.success(request, "Le nouveau cours a bien été ajouté")
            return redirect('cours:mes_cours')
    else:
        cours_form = CoursForm()  # Formulaire vide pour l'ajout de cours
        
    context = {
        'cours_form': cours_form
    }
    return render(request, 'cours/cours_form.html', context)

# Vue pour modifier un cours existant
@login_required
def update_cours(request, id):
    cours = Cours.objects.get(id=id)  # Récupération du cours à modifier
    # Vérification que l'utilisateur connecté est bien l'enseignant du cours
    if cours.enseignant != request.user:
        messages.error(request, "Vous ne pouvez pas modifier un cours qui ne vous appartient pas")
        return redirect('cours:mes_cours')
    
    # Si la requête est de type POST (soumission du formulaire de modification)
    if request.method == 'POST':
        cours_form = CoursForm(request.POST, instance=cours)
        if cours_form.is_valid():
            cours_update = cours_form.save(commit=False)
            cours_update.enseignant = request.user  # On s'assure que l'enseignant reste le même
            cours_update.save()  # Sauvegarde des modifications
        
            messages.success(request, f"Le cours {cours.nom} a bien été modifié")
            return redirect('cours:mes_cours')
    else:
        cours_form = CoursForm(instance=cours)  # Formulaire pré-rempli avec les données du cours
        
    context = {
        'cours_form': cours_form,
        'cours': cours
    }
    return render(request, 'cours/cours_form.html', context)

# Vue pour supprimer un cours
@login_required
def delete_cours(request, id):
    cours = Cours.objects.get(id=id)  # Récupération du cours à supprimer
    # Vérification que l'utilisateur connecté est bien l'enseignant du cours
    if cours.enseignant != request.user:
        messages.error(request, "Vous ne pouvez pas supprimer un cours qui ne vous appartient pas")
    else:
        messages.success(request, f"La suppression du cours {cours.nom} s'est bien passée")
        cours.delete()  # Suppression du cours
    
    return redirect('cours:mes_cours')
