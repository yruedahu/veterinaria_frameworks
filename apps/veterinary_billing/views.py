from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from .forms import ClientForm
from django.utils import timezone

def billing_home(request):
    return render(request,'veterinary_billing/home_billing.html')

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'veterinary_billing/client_list.html', {'clients': clients})

# Crear cliente
def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'veterinary_billing/client_form.html', {'form': form})

# Editar cliente
def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'veterinary_billing/client_form.html', {'form': form})

# Eliminar cliente
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'veterinary_billing/client_confirm_delete.html', {'client': client})

# Generar factura
def generar_factura(request):
    if request.method == 'POST':
        # Recoge los datos del formulario
        cliente_nombre = request.POST.get('cliente_nombre')
        cliente_telefono = request.POST.get('cliente_telefono')
        cliente_direccion = request.POST.get('cliente_direccion')
        cliente_email = request.POST.get('cliente_email')
        mascota_nombre = request.POST.get('mascota_nombre')
        mascota_especie = request.POST.get('mascota_especie')
        mascota_raza = request.POST.get('mascota_raza')
        mascota_edad = request.POST.get('mascota_edad')
        servicio_descripcion = request.POST.get('servicio_descripcion')
        servicio_cantidad = int(request.POST.get('servicio_cantidad'))
        servicio_precio = float(request.POST.get('servicio_precio'))

        subtotal = servicio_cantidad * servicio_precio
        iva = subtotal * 0.19
        total = subtotal + iva

        contexto = {
            'cliente_nombre': cliente_nombre,
            'cliente_telefono': cliente_telefono,
            'cliente_direccion': cliente_direccion,
            'cliente_email': cliente_email,
            'mascota_nombre': mascota_nombre,
            'mascota_especie': mascota_especie,
            'mascota_raza': mascota_raza,
            'mascota_edad': mascota_edad,
            'servicio_descripcion': servicio_descripcion,
            'servicio_cantidad': servicio_cantidad,
            'servicio_precio': servicio_precio,
            'subtotal': subtotal,
            'iva': iva,
            'total': total,
        }
        # Renderiza la plantilla de la factura con los datos ingresados
        return render(request, 'veterinary_billing/factura_sencilla.html', contexto)
    else:
        return redirect('billing_home')  # O el nombre de tu vista de formulario

# Imprimir factura
def print_factura(request):
    # Aquí iría la lógica para imprimir la factura
    return render(request, 'veterinary_billing/print_factura.html')

# Guardar factura
def save_factura(request):
    # Aquí iría la lógica para guardar la factura
    return render(request, 'veterinary_billing/save_factura.html')

# Listar mascotas
def pets_list(request):
    pets = Pets.objects.all()
    return render(request, 'veterinary_billing/pets_list.html', {'pets': pets})

# Crear mascota
def pets_create(request):
    if request.method == 'POST':
        form = PetsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pets_list')
    else:
        form = PetsForm()
    return render(request, 'veterinary_billing/pets_form.html', {'form': form})

# Editar mascota
def pets_update(request, pk):
    pet = get_object_or_404(Pets, pk=pk)
    if request.method == 'POST':
        form = PetsForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pets_list')
    else:
        form = PetsForm(instance=pet)
    return render(request, 'veterinary_billing/pets_form.html', {'form': form})

# Eliminar mascota
def pets_delete(request, pk):
    pet = get_object_or_404(Pets, pk=pk)
    if request.method == 'POST':
        pet.delete()
        return redirect('pets_list')
    return render(request, 'veterinary_billing/pets_confirm_delete.html', {'pet': pet})

def gen_factura(request):
    if request.method == 'POST':
        return redirect('billing_home')
    context = {
        'fecha': timezone.now().date(),
    }
    return render(request, 'veterinary_billing/gen_factura.html', context)

# Aquí iría la lógica para manejar las facturas, como generar, imprimir y guardar
# Aquí iría la lógica para manejar las mascotas, como crear, editar y eliminar
# Aquí iría la lógica para manejar los servicios, como crear, editar y eliminar
# Aquí iría la lógica para manejar los pagos, como registrar y verificar pagos