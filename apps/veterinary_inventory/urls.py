from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_home, name='home_inventory'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
