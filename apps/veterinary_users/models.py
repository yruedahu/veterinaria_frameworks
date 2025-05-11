from django.db import models

# Create your models here.

class Perfil(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    tipoDocumento = [
        ('CC', 'Cédula de ciudadanía'),
        ('TI', 'Tarjeta de identidad'),
        ('CE', 'Cédula de extranjería'),
        ('NIT', 'NIT'),
    ]
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    tipodocumento = models.CharField(max_length=3, choices=tipoDocumento)
    numerodocumento = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(unique=True)
    celular = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)
    rol = models.ForeignKey(Perfil, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class UserAccount(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, unique=True)
    contrasena = models.CharField(max_length=128) 
    activo = models.BooleanField(default=True)
    fecharegistro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class UserActivity(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    accion = models.CharField(max_length=255)
    horainstantanea = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.accion}..."

class UserMessage(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    mensaje = models.TextField()
    visto = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Para {self.usuario.nombres} - {self.titulo}"
