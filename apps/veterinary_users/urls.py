from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_users, name='home_users'),
    path('registrar/', views.registro_usuarios, name='registro_usuarios'),
    path('cuentausuario/', views.cuenta_usuarios, name='cuenta_usuarios')
]
