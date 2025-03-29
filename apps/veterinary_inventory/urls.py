from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_home, name='home_inventory'),
]
