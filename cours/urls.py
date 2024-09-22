from django.urls import path
from . import views

# Déclaration du namespace pour l'application 'cours'
app_name = 'cours'

# Liste des routes URL (urlpatterns)
urlpatterns = [
    # Route pour la page d'accueil (home)
    path('', views.home, name='home'),  # Cette URL correspond à la vue 'home'

    # Route pour la page de connexion
    path('login/', views.login_system, name='login'),  # Cette URL correspond à la vue 'login_system'

    # Route pour la page d'inscription
    path('register/', views.register, name='register'),  # Cette URL correspond à la vue 'register'

    # Route pour afficher les cours de l'utilisateur connecté
    path('mes_cours/', views.mes_cours, name='mes_cours'),  # Cette URL correspond à la vue 'mes_cours'

    # Route pour ajouter un nouveau cours
    path('add_cours/', views.add_cours, name='add_cours'),  # Cette URL correspond à la vue 'add_cours'

    # Route pour modifier un cours existant, l'ID du cours est passé en paramètre
    path('update_cours/<int:id>/', views.update_cours, name='update_cours'),  # Cette URL correspond à la vue 'update_cours'

    # Route pour supprimer un cours, l'ID du cours est passé en paramètre
    path('delete_cours/<int:id>/', views.delete_cours, name='delete_cours'),  # Cette URL correspond à la vue 'delete_cours'
]
