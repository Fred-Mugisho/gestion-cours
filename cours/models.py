from django.db import models
from django.contrib.auth.models import User

class Cours(models.Model):
    enseignant = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.nom