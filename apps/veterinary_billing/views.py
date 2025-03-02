from django.shortcuts import render
from django.http import HttpResponse

def billing_home(request):
    return HttpResponse("¡Veterinary Billing está funcionando!")