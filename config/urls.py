from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.veterinary_home.urls')),
    path('users/', include('apps.veterinary_users.urls')),
    path('pets/', include('apps.veterinary_pets.urls')),
    path('clinic/', include('apps.veterinary_clinic.urls')),
    path('billing/', include('apps.veterinary_billing.urls')),
    path('inventory/', include('apps.veterinary_inventory.urls')),
]
