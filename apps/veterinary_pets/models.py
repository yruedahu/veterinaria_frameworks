from django.db import models

class Owner(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.full_name


class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField()
    born_date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    vaccinated = models.BooleanField(default=False)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="pets")

    def __str__(self):
        return f"{self.name} ({self.species})"


class MedicalRecord(models.Model):
    pet = models.OneToOneField(Pet, on_delete=models.CASCADE, related_name="medical_record")
    notes = models.TextField()
    allergies = models.TextField(blank=True)
    chronic_conditions = models.TextField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Historial Médico de {self.pet.name}"


class Appointment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    date = models.DateTimeField()
    reason = models.TextField()
    veterinarian = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Pendiente'),
        ('completed', 'Completada'),
        ('cancelled', 'Cancelada')
    ])

    def __str__(self):
        return f"Cita: {self.pet.name} - {self.date.strftime('%d/%m/%Y')}"


class Vaccination(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    vaccine_name = models.CharField(max_length=100)
    date_administered = models.DateField()
    veterinarian = models.CharField(max_length=100)

    def __str__(self):
        return f"Vacuna {self.vaccine_name} para {self.pet.name}"
