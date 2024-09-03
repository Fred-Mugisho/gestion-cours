from django.shortcuts import render

# Create your views here.

def home(request):
    nom = "toto"
    context = {
        'nom': nom
    }
    return render(request, 'cours/home.html', context)