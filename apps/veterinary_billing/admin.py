from django.contrib import admin
from .models import Client, Pets, Service, Invoice

# Register your models here.
admin.site.register(Client)
admin.site.register(Pets)
admin.site.register(Service)
admin.site.register(Invoice)

