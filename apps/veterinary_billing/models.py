from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre_Cliente = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.nombre_cliente

class Mascota (models.Model):
    nombre = models.CharField(max_length=255)
    especie = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    edad = models.IntegerField()
    
    def __str__(self):
        return self.nombre

class Factura (models.Model):
    numero_factura = models.CharField (max_length=20)
    descripcion = models.TextField()
    cantidad = models.IntegerField()
    precio = models.DecimalField (max_digits=10, decimal_places=2)              
    
    def __str__(self):
        return self.numero_factura
    
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