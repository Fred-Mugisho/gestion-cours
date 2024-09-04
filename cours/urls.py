from django.urls import path
from . import views

app_name = 'cours'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_system, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
