from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.db.models import Count
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Appointment
from .forms import AppointmentForm, AppointmentUpdateForm, AppointmentFilterForm
import json
from datetime import datetime, timedelta
from django.db.models import Q

def clinic_home(request):
    return render(request, 'veterinary_clinic/appointments_home.html', {})

class AppointmentListView(ListView):
    model = Appointment
    template_name = 'veterinary_clinic/appointment_list.html'
    context_object_name = 'appointments'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = AppointmentFilterForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = Appointment.objects.all()
        form = AppointmentFilterForm(self.request.GET)
        
        if form.is_valid():
            filter_by = form.cleaned_data.get('filter_by')
            search = form.cleaned_data.get('search')
            date_from = form.cleaned_data.get('date_from')
            date_to = form.cleaned_data.get('date_to')
            appointment_type = form.cleaned_data.get('appointment_type')

            if filter_by == 'today':
                queryset = queryset.filter(appointment_date=timezone.now().date())
            elif filter_by == 'week':
                week_start = timezone.now().date()
                week_end = week_start + timedelta(days=7)
                queryset = queryset.filter(appointment_date__range=[week_start, week_end])
            elif filter_by == 'month':
                month_start = timezone.now().date().replace(day=1)
                if month_start.month == 12:
                    month_end = month_start.replace(year=month_start.year + 1, month=1) - timedelta(days=1)
                else:
                    month_end = month_start.replace(month=month_start.month + 1) - timedelta(days=1)
                queryset = queryset.filter(appointment_date__range=[month_start, month_end])
            elif filter_by == 'pending':
                queryset = queryset.filter(status='PENDING')
            elif filter_by == 'completed':
                queryset = queryset.filter(status='COMPLETED')

            if search:
                queryset = queryset.filter(
                    Q(pet_name__icontains=search) |
                    Q(owner_name__icontains=search)
                )

            if date_from:
                queryset = queryset.filter(appointment_date__gte=date_from)
            if date_to:
                queryset = queryset.filter(appointment_date__lte=date_to)
            if appointment_type:
                queryset = queryset.filter(appointment_type=appointment_type)

        return queryset.order_by('appointment_date', 'appointment_time')

class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'veterinary_clinic/appointment_form.html'
    success_url = reverse_lazy('appointment_list')

    def form_valid(self, form):
        messages.success(self.request, 'Cita creada exitosamente.')
        return super().form_valid(form)

class AppointmentUpdateView(UpdateView):
    model = Appointment
    form_class = AppointmentUpdateForm
    template_name = 'veterinary_clinic/appointment_form.html'
    success_url = reverse_lazy('appointment_list')

    def form_valid(self, form):
        messages.success(self.request, 'Cita actualizada exitosamente.')
        return super().form_valid(form)

class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'veterinary_clinic/appointment_confirm_delete.html'
    success_url = reverse_lazy('appointment_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Cita eliminada exitosamente.')
        return super().delete(request, *args, **kwargs)

class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'veterinary_clinic/appointment_detail.html'
    context_object_name = 'appointment'

def appointment_calendar(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        start = request.GET.get('start')
        end = request.GET.get('end')
        
        if start and end:
            start_date = datetime.strptime(start[:10], '%Y-%m-%d')
            end_date = datetime.strptime(end[:10], '%Y-%m-%d')
            appointments = Appointment.objects.filter(
                appointment_date__range=[start_date, end_date]
            )
        else:
            appointments = Appointment.objects.all()

        events = []
        for appointment in appointments:
            events.append({
                'id': appointment.id,
                'title': f"{appointment.pet_name} - {appointment.get_appointment_type_display()}",
                'start': f"{appointment.appointment_date}T{appointment.appointment_time}",
                'status': appointment.status,
                'pet_name': appointment.pet_name,
                'owner_name': appointment.owner_name,
                'appointment_type': appointment.get_appointment_type_display(),
                'symptoms': appointment.symptoms or '',
                'notes': appointment.notes or '',
                'className': f'status-{appointment.status.lower()}'
            })

        return JsonResponse(events, safe=False)
    return render(request, 'veterinary_clinic/appointment_calendar.html')

def appointment_calendar_events(request):
    print("Fetching calendar events...")
    appointments = Appointment.objects.all()
    print(f"Found {appointments.count()} appointments")

    events = []
    for appointment in appointments:
        # Format the date and time properly
        appointment_datetime = datetime.combine(
            appointment.appointment_date,
            appointment.appointment_time
        )
        
        event = {
            'id': appointment.id,
            'title': f"{appointment.pet_name} - {appointment.get_appointment_type_display()}",
            'start': appointment_datetime.strftime('%Y-%m-%dT%H:%M:%S'),
            'extendedProps': {
                'status': appointment.status,
                'pet_name': appointment.pet_name,
                'owner_name': appointment.owner_name,
                'appointment_type': appointment.get_appointment_type_display(),
                'symptoms': appointment.symptoms or '',
                'notes': appointment.notes or ''
            },
            'className': f'status-{appointment.status.lower()}'
        }
        events.append(event)
        print(f"Added event: {event}")

    return JsonResponse(events, safe=False)

def appointment_dashboard(request):
    today = timezone.now().date()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(days=6)

    context = {
        'total_appointments': Appointment.objects.count(),
        'pending_appointments': Appointment.objects.filter(status='PENDING').count(),
        'today_appointments': Appointment.objects.filter(appointment_date=today).count(),
        'week_appointments': Appointment.objects.filter(
            appointment_date__range=[week_start, week_end]
        ).count(),
        
        'appointments_by_type': json.dumps(list(
            Appointment.objects.values('appointment_type')
            .annotate(count=Count('id'))
            .values('appointment_type', 'count')
        )),
        
        'appointments_by_status': json.dumps(list(
            Appointment.objects.values('status')
            .annotate(count=Count('id'))
            .values('status', 'count')
        )),
        
        'recent_appointments': Appointment.objects.filter(
            appointment_date__gte=today
        ).order_by('appointment_date', 'appointment_time')[:5]
    }
    
    return render(request, 'veterinary_clinic/appointment_dashboard.html', context)