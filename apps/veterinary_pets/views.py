from django.shortcuts import render
from django.http import HttpResponse

def pets_home(request):
    return render(request,'veterinary_pets/home_pets.html')