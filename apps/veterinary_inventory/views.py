from django.shortcuts import render
from django.http import HttpResponse

def inventory_home(request):
    return HttpResponse("¡Veterinary pets está funcionando!")