from django.urls import path
from . import views

urlpatterns = [
    path('', views.pets_home, name='home_pets'),
    path('pet/<int:pet_id>/', views.pet_detail, name='pet_detail'),
    path('pets/create_pet/', views.create_pet, name='create_pet'),
    path('pet/<int:pet_id>/medical_record/', views.medical_record_detail, name='medical_record_detail'),
    path('pet/<int:pet_id>/medical_record/edit/', views.medical_record_edit, name='medical_record_edit'),
]
