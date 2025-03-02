from django.shortcuts import render
from django.http import HttpResponse

def pets_home(request):
    return HttpResponse("¡Veterinary pets está funcionando!")