from django.urls import path
from . import views

urlpatterns = [
    path('', views.clinic_home, name='home_appointments'),
    path('list/', views.AppointmentListView.as_view(), name='appointment_list'),
    path('create/', views.AppointmentCreateView.as_view(), name='create_appointment'),
    path('<int:pk>/update/', views.AppointmentUpdateView.as_view(), name='appointment_update'),
    path('<int:pk>/delete/', views.AppointmentDeleteView.as_view(), name='appointment_delete'),
    path('<int:pk>/', views.AppointmentDetailView.as_view(), name='appointment_detail'),
    path('calendar/', views.appointment_calendar, name='appointment_calendar'),
    path('calendar/events/', views.appointment_calendar_events, name='appointment_calendar_events'),
    path('dashboard/', views.appointment_dashboard, name='appointment_dashboard'),
]
