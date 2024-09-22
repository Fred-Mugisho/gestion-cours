# Introduction aux Applications Web

Ce projet vise à présenter les fondamentaux du développement d'applications web en utilisant des technologies modernes. Il a été développé avec **Django**, **Python**, et stylisé avec **Tailwind CSS**.

## 1. Technologies Utilisées
- **Django / Python** : Framework web puissant et flexible.
- **Tailwind CSS** : Framework CSS pour une conception rapide et réactive.
- **HTML / CSS / JavaScript** : Langages de base pour la création de pages web interactives.

## 2. Liens Utiles
- **Dépôt GitHub** : [Gestion Cours Repository](https://github.com/Fred-Mugisho/gestion-cours)
- **Documentation Tailwind CSS** : [Tailwind CSS](https://tailwindcss.com/)
- **Site Officiel de Django** : [Django](https://www.djangoproject.com)
- **Site Officiel de Python** : [Python](https://www.python.org)
- **W3Schools HTML** : [HTML](https://www.w3schools.com)
- **W3Schools CSS** : [CSS](https://www.w3schools.com)
- **W3Schools JavaScript** : [JavaScript](https://www.w3schools.com)
- **Documentation Git** : [Git](https://git-scm.com/doc)

## 3. Étapes de Création du Projet Django

### A. Créer un Environnement Virtuel
```bash
python -m venv web_env
web_env\Scripts\activate  # Pour Windows
# source web_env/bin/activate  # Pour MacOS/Linux
```

### B. Créer le Projet Django
```bash
pip install Django
django-admin startproject gestion_cours
cd gestion_cours
python manage.py runserver
# Arrêter le serveur avec Ctrl + C
python manage.py makemigrations
python manage.py migrate
python manage.py startapp cours
```

## 4. Configuration du Projet Django

### A. Ajouter une Nouvelle Application
#### Ouvrez le fichier ```bash settings.py``` et ajoutez l'application :
```bash
INSTALLED_APPS = [
    ...
    'cours.apps.CoursConfig',
]
```

#### Dans le fichier ```bash urls.py``` du projet, incluez les URLs de l'application :
```bash
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cours.urls')),
]
```

### B. Configurer les Templates de Django
#### Créez un dossier ```bash templates``` dans votre projet.
#### Dans ```bash settings.py```, ajoutez le chemin vers le dossier de templates dans DIRS :
```bash 
TEMPLATES = [
    ...
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        ...
    },
]
```

### C. Ajouter des Fichiers Statiques
#### Dans ```bash settings.py```, configurez les fichiers statiques :
```bash
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```