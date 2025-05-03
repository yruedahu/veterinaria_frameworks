from django.contrib import admin
from .models import Cliente, Mascota, Factura

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Mascota)
admin.site.register(Factura)

