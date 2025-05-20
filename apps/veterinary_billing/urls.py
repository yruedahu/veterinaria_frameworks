from django.urls import path
from . import views

urlpatterns = [
    path('', views.billing_home, name='billing_home'),
    path('invoice/<int:invoice_id>/', views.invoice_detail, name='invoice_detail'),
]
# Compare this snippet from apps/veterinary_billing/views.py:
# from django.shortcuts import render