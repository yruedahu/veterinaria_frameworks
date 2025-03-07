from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_users, name='home_users'),
]
