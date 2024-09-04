from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    nom = "toto"
    context = {
        'nom': nom
    }
    return render(request, 'cours/home.html', context)

def login_system(request):
    if request.method == 'POST':
        print(request.POST)
        return redirect('cours:dashboard')
    
    return render(request, 'cours/login.html')

def register(request):
    return render(request, 'cours/register.html')

def dashboard(request):
    return render(request, 'cours/dashboard.html')