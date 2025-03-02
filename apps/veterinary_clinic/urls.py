from django.urls import path
from . import views

urlpatterns = [
    path('', views.clinic_home, name='clinic_home'),
]
