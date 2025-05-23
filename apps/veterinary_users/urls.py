from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_users, name='home_users'),
    path('registrar/', views.registro_usuarios, name='registro_usuarios'),
    path('cuentausuario/<int:usuario_id>/', views.cuenta_usuarios, name='cuenta_usuarios'),
    path('actualizarusuario/<int:usuario_id>/', views.actualizar_usuarios, name='actualizar_usuarios'),
    path('actualizarcontrasena/<int:useraccount_id>/', views.actualizar_contrasena, name='actualizar_contrasena'),
    path('rol/<int:useraccount_id>/', views.rol, name='rol'),
    path('editarrol/<int:rol_id>/<int:useraccount_id>/', views.editar_rol, name='editar_rol'),
    path('dashboard/<int:useraccount_id>/', views.dashboard, name='dashboard'),
]
