from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pets/', include('apps.veterinary_pets.urls')),
    path('users/', include('apps.veterinary_users.urls')),
    path('clinic/', include('apps.veterinary_clinic.urls')),
    path('billing/', include('apps.veterinary_billing.urls')),
    path('inventory/', include('apps.veterinary_inventory.urls')),
]
