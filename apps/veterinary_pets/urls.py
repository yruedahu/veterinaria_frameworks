from django.urls import path
from . import views

urlpatterns = [
    path('', views.pets_home, name='pets_home'),
]
