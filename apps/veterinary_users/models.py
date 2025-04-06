from django.db import models

# Create your models here.

# 1. Rol de Usuario
class UserRole(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# 2. Usuario
class User(models.Model):
    id = models.AutoField(primary_key=True)

    DOCUMENT_TYPES = [
        ('CC', 'Cédula de ciudadanía'),
        ('TI', 'Tarjeta de identidad'),
        ('CE', 'Cédula de extranjería'),
        ('NIT', 'NIT'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    document_type = models.CharField(max_length=3, choices=DOCUMENT_TYPES)
    document_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    role = models.ForeignKey(UserRole, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# 3. Cuenta de Usuario
class UserAccount(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

# 4. Historial de Actividades del Usuario
class UserActivity(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.action[:20]}..."

# 5. Mensajes o Notificaciones
class UserMessage(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Para {self.user.first_name} - {self.subject}"
