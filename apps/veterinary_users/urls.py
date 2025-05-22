from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_users, name='home_users'),
    path('registrar/', views.registro_usuarios, name='registro_usuarios'),
    path('cuentausuario/', views.cuenta_usuarios, name='cuenta_usuarios'),
    path('actualizarusuario/', views.actualizar_usuarios, name='actualizar_usuarios'),
    path('actualizarcontrasena/', views.actualizar_contrasena, name='actualizar_contrasena'),
    path('rol/', views.rol, name='rol'),
    path('editarrol/', views.editar_rol, name='editar_rol'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
