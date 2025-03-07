from django.shortcuts import render
from django.http import HttpResponse

def home_users(request):
    return render(request,'veterinary_users/home_users.html')
