from django.urls import path
from . import views

urlpatterns = [
    path('', views.billing_home, name='billing_home'),
    path('billing_home/', views.billing_home, name='billing_home'),
    path('clients/', views.client_list, name='client_list'), 
    path('clients/create/', views.client_create, name='client_create'),  
    path('clients/<int:pk>/edit/', views.client_update, name='client_update'),  
    path('clients/<int:pk>/delete/', views.client_delete, name='client_delete'),  
    path('gen_factura/', views.gen_factura, name='gen_factura'),
    path('generar/', views.generar_factura, name='generar_factura'),
    path('imprimir/', views.print_factura, name='print_factura'),  
    path('guardar/', views.save_factura, name='save_factura'),
    path('pets/', views.pets_list, name='pets_list'),
    path('pets/create/', views.pets_create, name='pets_create'),
    path('pets/<int:pk>/edit/', views.pets_update, name='pets_update'),
    path('pets/<int:pk>/delete/', views.pets_delete, name='pets_delete'),
]       