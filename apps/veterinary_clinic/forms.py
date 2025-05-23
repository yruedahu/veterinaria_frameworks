from django import forms
from .models import Appointment
from django.utils import timezone
from datetime import datetime, time

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'pet_name', 'owner_name', 'owner_phone', 'owner_email',
            'appointment_type', 'appointment_date', 'appointment_time',
            'symptoms', 'notes'
        ]
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time'}),
            'symptoms': forms.Textarea(attrs={'rows': 3}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_appointment_date(self):
        date = self.cleaned_data['appointment_date']
        if date < timezone.localdate():
            raise forms.ValidationError('No puedes agendar citas en fechas pasadas')
        return date

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('appointment_date')
        time = cleaned_data.get('appointment_time')
        
        if date and time:
            # Crear un datetime consciente de la zona horaria
            datetime_combined = timezone.make_aware(
                datetime.combine(date, time)
            )
            if datetime_combined < timezone.now():
                raise forms.ValidationError('No puedes agendar citas en fechas y horas pasadas')
        return cleaned_data

class AppointmentUpdateForm(AppointmentForm):
    status = forms.ChoiceField(
        choices=Appointment.APPOINTMENT_STATUS,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta(AppointmentForm.Meta):
        fields = AppointmentForm.Meta.fields + ['status']

class AppointmentFilterForm(forms.Form):
    FILTER_CHOICES = [
        ('all', 'Todas las Citas'),
        ('today', 'Citas de Hoy'),
        ('week', 'Citas de esta Semana'),
        ('month', 'Citas de este Mes'),
        ('pending', 'Citas Pendientes'),
        ('completed', 'Citas Completadas'),
    ]

    filter_by = forms.ChoiceField(
        choices=FILTER_CHOICES,
        required=False,
        initial='all',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar por nombre de mascota o dueño'
        })
    )
    
    date_from = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    
    date_to = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    
    appointment_type = forms.ChoiceField(
        choices=[('', 'Todos los tipos')] + Appointment.APPOINTMENT_TYPE,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    ) 