from django.db import models
from django.contrib.auth.models import User

# Définition du modèle Cours
class Cours(models.Model):
    # Relation entre le cours et l'utilisateur (enseignant)
    # Chaque cours est lié à un enseignant via une clé étrangère (ForeignKey)
    # Si l'enseignant est supprimé, tous les cours associés seront également supprimés (on_delete=models.CASCADE)
    enseignant = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Le nom du cours (une chaîne de caractères avec une limite de 100 caractères)
    nom = models.CharField(max_length=100)
    
    # Une description du cours, sans limite de longueur
    description = models.TextField()
    
    # Date et heure de création du cours (remplie automatiquement lors de la création)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Date et heure de la dernière modification du cours (mise à jour automatiquement à chaque modification)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Méthode pour afficher le nom du cours comme représentation sous forme de chaîne
    def __str__(self) -> str:
        return self.nom
