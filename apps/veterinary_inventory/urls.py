from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_home, name='home_inventory'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('products/export/<str:filetype>/', views.export_products, name='export_products'),
    path('products/import/', views.import_products, name='import_products'),
    path('stock-alerts/', views.product_stock_alerts, name='product_stock_alerts'),
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('suppliers/create/', views.supplier_create, name='supplier_create'),
    path('suppliers/<int:pk>/edit/', views.supplier_edit, name='supplier_edit'),
    path('suppliers/<int:pk>/delete/', views.supplier_delete, name='supplier_delete'),
    path('suppliers/export/<str:filetype>/', views.export_suppliers, name='export_suppliers'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
    path('movements/', views.movement_list, name='movement_list'),
    path('movements/create/', views.movement_create, name='movement_create'),
    path('movements/export/<str:filetype>/', views.export_movements, name='export_movements'),
    path('dashboard/', views.inventory_dashboard, name='inventory_dashboard'),
    path('export/stock-alerts/<str:format>/', views.export_stock_alerts, name='export_stock_alerts'),
]
