from django.urls import path
from . import views

urlpatterns = [
    path('', views.billing_home, name='billing_home'),
]
