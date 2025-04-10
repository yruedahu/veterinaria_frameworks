from django.urls import path
from . import views

urlpatterns = [
    path('', views.pets_home, name='home_pets'),
    path('pet/<int:pet_id>/', views.pet_detail, name='pet_detail'),
]
