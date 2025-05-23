from django.db import models
from django.utils import timezone

# Create your models here.

class Appointment(models.Model):
    APPOINTMENT_STATUS = [
        ('PENDING', 'Pendiente'),
        ('CONFIRMED', 'Confirmada'),
        ('COMPLETED', 'Completada'),
        ('CANCELLED', 'Cancelada'),
    ]

    APPOINTMENT_TYPE = [
        ('GENERAL', 'Consulta General'),
        ('EMERGENCY', 'Emergencia'),
        ('VACCINATION', 'Vacunación'),
        ('GROOMING', 'Peluquería'),
        ('SURGERY', 'Cirugía'),
        ('CHECKUP', 'Control'),
    ]

    pet_name = models.CharField(max_length=100, verbose_name='Nombre de la Mascota')
    owner_name = models.CharField(max_length=100, verbose_name='Nombre del Dueño')
    owner_phone = models.CharField(max_length=20, verbose_name='Teléfono del Dueño')
    owner_email = models.EmailField(verbose_name='Email del Dueño')
    
    appointment_type = models.CharField(
        max_length=20,
        choices=APPOINTMENT_TYPE,
        default='GENERAL',
        verbose_name='Tipo de Cita'
    )
    
    appointment_date = models.DateField(verbose_name='Fecha de la Cita')
    appointment_time = models.TimeField(verbose_name='Hora de la Cita')
    
    status = models.CharField(
        max_length=20,
        choices=APPOINTMENT_STATUS,
        default='PENDING',
        verbose_name='Estado'
    )
    
    symptoms = models.TextField(blank=True, null=True, verbose_name='Síntomas')
    notes = models.TextField(blank=True, null=True, verbose_name='Notas Adicionales')
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última Actualización')

    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
        ordering = ['-appointment_date', '-appointment_time']

    def __str__(self):
        return f"Cita de {self.pet_name} - {self.get_appointment_type_display()} - {self.appointment_date}"

    def is_upcoming(self):
        today = timezone.now().date()
        return self.appointment_date >= today and self.status not in ['COMPLETED', 'CANCELLED']

    def can_be_cancelled(self):
        return self.status in ['PENDING', 'CONFIRMED']

    def can_be_edited(self):
        return self.status not in ['COMPLETED', 'CANCELLED']
