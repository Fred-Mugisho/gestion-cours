from django import forms
from .models import *

# Définition du formulaire pour le modèle 'Cours'
class CoursForm(forms.ModelForm):

    # Champ pour le nom du cours
    # - CharField est utilisé pour des champs de texte courts
    # - Le widget TextInput permet de personnaliser l'apparence du champ via des attributs HTML
    nom = forms.CharField(
        label="Nom du cours",  # Le texte du label affiché pour ce champ
        widget=forms.TextInput(attrs={
            'class': "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500",  # Classe CSS pour le style du champ
        })
    )

    # Champ pour la description du cours
    # - CharField avec un widget Textarea permet d'avoir une zone de texte multi-lignes
    description = forms.CharField(
        label="Description du cours",  # Le texte du label pour ce champ
        widget=forms.Textarea(attrs={
            'class': "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500",  # Classes CSS pour le style du champ
            'rows': '4'  # Définition de la taille visible du textarea avec 4 lignes
        })
    )
    
    # Classe Meta pour lier ce formulaire au modèle et spécifier les champs
    class Meta:
        model = Cours  # Le modèle associé à ce formulaire est 'Cours'
        fields = ('nom', 'description')  # Les champs du modèle à inclure dans le formulaire
