from django.shortcuts import render, get_object_or_404
from .models import Pet

def pets_home(request):
    return render(request,'veterinary_pets/home_pets.html')

def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)

    pets = {
        'pet': pet,
        'owner': pet.owner.full_name,
        'email': pet.owner.email,
        'phone': pet.owner.phone,
        'address': pet.owner.address,
    }
    return render(request, 'veterinary_pets/pet_detail.html', pets)