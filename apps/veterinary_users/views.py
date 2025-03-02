from django.shortcuts import render
from django.http import HttpResponse

def users_home(request):
    return HttpResponse("¡Veterinary pets está funcionando!")
