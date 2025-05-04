from django.shortcuts import render
from django.http import HttpResponse

def home_users(request):
    return render(request,'veterinary_users/home_users.html')

def registro_usuarios(request):
    return render(request, 'veterinary_users/registro_usuarios.html')

def cuenta_usuarios(request):
    return render(request, 'veterinary_users/cuenta_usuarios.html')