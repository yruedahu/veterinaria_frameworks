from django.shortcuts import render
from django.http import HttpResponse 

def billing_home(request):
    return render (request,'veterinary_billing/home_billing.html')