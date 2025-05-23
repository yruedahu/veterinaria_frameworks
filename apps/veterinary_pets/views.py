from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect  # Import necesario para redirección
from django.contrib import messages  # Import necesario para mensajes flash
from .models import Pet, Owner, MedicalRecord, MedicalAttachment
from django.core.files.storage import FileSystemStorage

def pets_home(request):
    return render(request,'veterinary_pets/home_pets.html')

def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    next_pet = Pet.objects.filter(id__gt=pet_id).order_by('id').first()
    prev_pet = Pet.objects.filter(id__lt=pet_id).order_by('-id').first()

    pets = {
        'pet': pet,
        'owner': pet.owner.full_name,
        'email': pet.owner.email,
        'phone': pet.owner.phone,
        'address': pet.owner.address,
        'next_pet': next_pet,
        'prev_pet': prev_pet
    }
    return render(request, 'veterinary_pets/pet_detail.html', pets)

def create_pet(request):
    if request.method == 'POST':
        try:
            # Crear o recuperar el propietario
            owner, created = Owner.objects.get_or_create(
                full_name=request.POST['owner_name'],
                phone=request.POST['owner_phone'],
                email=request.POST.get('owner_email', ''),
                address=request.POST.get('owner_address', '')
            )

            # Crear la mascota
            pet = Pet.objects.create(
                name=request.POST['pet_name'],
                species=request.POST['pet_species'],
                breed=request.POST.get('pet_breed', ''),
                age=request.POST['pet_age'],
                born_date=request.POST['pet_born_date'],
                weight=request.POST.get('pet_weight', None),
                vaccinated='pet_vaccinated' in request.POST,
                owner=owner
            )

            messages.success(request, f"La mascota {pet.name} ha sido registrada exitosamente.")
        except Exception as e:
            messages.error(request, "Ocurrió un error al registrar la mascota. Por favor, inténtalo de nuevo.")

        return HttpResponseRedirect('/')

    return render(request, 'veterinary_pets/home_pets.html')

def medical_record_detail(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    medical_record = getattr(pet, 'medical_record', None)
    attachments = medical_record.attachments.all() if medical_record else []
    return render(request, 'veterinary_pets/medical_record_detail.html', {
        'pet': pet,
        'medical_record': medical_record,
        'attachments': attachments
    })

def medical_record_edit(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    medical_record = getattr(pet, 'medical_record', None)
    if request.method == 'POST':
        notes = request.POST.get('notes', '')
        allergies = request.POST.get('allergies', '')
        chronic_conditions = request.POST.get('chronic_conditions', '')
        if not medical_record:
            medical_record = MedicalRecord.objects.create(pet=pet, notes=notes, allergies=allergies, chronic_conditions=chronic_conditions)
        else:
            medical_record.notes = notes
            medical_record.allergies = allergies
            medical_record.chronic_conditions = chronic_conditions
            medical_record.save()
        # Manejo de archivos adjuntos
        for f in request.FILES.getlist('attachments'):
            MedicalAttachment.objects.create(medical_record=medical_record, file=f)
        messages.success(request, 'Historial médico actualizado.')
        return HttpResponseRedirect(f'/pet/{pet.id}/medical_record/')
    return render(request, 'veterinary_pets/medical_record_form.html', {
        'pet': pet,
        'medical_record': medical_record
    })