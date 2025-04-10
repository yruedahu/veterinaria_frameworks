from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_users, name='home_users'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuario/<int:usuario_id>/', views.detalle_usuario, name='detalle_usuario'),
]
