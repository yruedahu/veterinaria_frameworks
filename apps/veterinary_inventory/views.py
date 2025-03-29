from django.shortcuts import render
from django.http import HttpResponse

def inventory_home(request):
    return render(request, 'veterinary_inventory/inventory_home.html')