from django.contrib import admin
from .models import Pet, Owner, MedicalRecord, Vaccination, Appointment, MedicalAttachment

admin.site.register(Pet)
admin.site.register(Owner)
admin.site.register(MedicalRecord)
admin.site.register(Vaccination)
admin.site.register(Appointment)
admin.site.register(MedicalAttachment)