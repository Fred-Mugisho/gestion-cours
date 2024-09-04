# Introduction aux applications web

## 1. Les technologies utilisées
### -> Django / Python
### -> Tailwind CSS
### -> HTML / CSS / JavaScript

## 2. Liens
### Repo github --> https://github.com/Fred-Mugisho/gestion-cours
### Tailwind CSS --> https://tailwindcss.com/
### Django --> https://www.djangoproject.com
### Python --> https://www.python.org
### HTML --> https://www.w3schools.com
### CSS --> https://www.w3schools.com
### JavaScript --> https://www.w3schools.com
### Github --> https://git-scm.com/doc


## 3. Etapes de creation du projet django

### A. Creer et  environnement virtuel
#### python -m venv web_env
#### web_env\Scripts\activate

### B. Creer app projet django
#### pip install Django
#### django-admin startproject gestion_cours
#### cd gestion_cours
#### python manage.py runserver
#### ctrl + c
#### python manage.py makemigrations
#### python manage.py migrate
#### python manage.py startapp cours

## 4. Configuration du projet django
### Pour ajouter un nouvel app dans le projet django
#### Aller dans le fichier settings.py et ajouter la nouvelle app
##### INSTALLED_APPS = [
#####     .....
#####     'cours.apps.CoursConfig',
##### ]
### Aller dans le fichier urls du projet et ajouter l'urls de la nouvelle app
##### from django.urls import path, include
##### from django.contrib import admin
#### urlpatterns = [
####     path('admin/', admin.site.urls),
####     path('', include('cours.urls'))
#### ]

### Pour configurer les templates de django
#### Creer un dossier templates dans votre projet
#### Aller dans le fichier settings.py et ajouter la nouvelle template dans la liste DIRS
##### TEMPLATES = [
#####     .....
#####     {
#####         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#####         'DIRS': [
#####              BASE_DIR / 'templates' 
#####          ],
#####         .....
#####     },
##### ]

### Pour ajouter les fichiers statiques dans le projet django
#### Aller dans le fichier settings.py et ajouter la nouvelle app
##### STATICFILES_DIRS = [
#####    BASE_DIR / 'static',
##### ]
