from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Pets(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.IntegerField()
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.species})"

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class Invoice(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pets, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)
    date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True, null=True) 

    def __str__(self):
        return f"Factura #{self.id} - {self.client.name}"
    
# Tipos de Datos en Django
# CharField: models.CharField()
# Para almacenar cadenas de texto cortas o medianas.

# TextField: models.TextField()
# Para almacenar texto largo sin límite de longitud.

# IntegerField: models.IntegerField()
# Para almacenar números enteros.

# FloatField: models.FloatField()
# Para almacenar números de punto flotante.

# DecimalField: models.DecimalField()
# Para almacenar números decimales de precisión fija.

# BooleanField: models.BooleanField()
# Para almacenar valores verdadero/falso.

# DateField: models.DateField()
# Para almacenar fechas.

# DateTimeField: models.DateTimeField()
# Para almacenar fechas y horas.

# EmailField: models.EmailField()
# Para almacenar direcciones de correo electrónico.

# FileField: models.FileField()
# Para almacenar archivos subidos.

# ImageField: models.ImageField()
# Para almacenar imágenes subidas.

# BinaryField: models.BinaryField()
# Para almacenar datos binarios.

# DurationField: models.DurationField()
# Para almacenar períodos de tiempo.

# GenericIPAddressField: models.GenericIPAddressField()
# Para almacenar direcciones IP.

# PositiveIntegerField: models.PositiveIntegerField()
# Para almacenar números enteros positivos.