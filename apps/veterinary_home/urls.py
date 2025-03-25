from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pets/', include('apps.veterinary_pets.urls')),
    path('billing/', include('apps.veterinary_billing.urls')),
    path('users/', include('apps.veterinary_users.urls')),
]
