from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Usuario

def home_users(request):
    return render(request,'veterinary_users/home_users.html')

def lista_usuarios(request):
    # Obtener todos los usuarios registrados
    usuarios = Usuario.objects.all()
    
    context = {
        'usuarios': usuarios,
        'total_usuarios': usuarios.count(),  # Número total de usuarios
    }
    return render(request, 'veterinary_users/lista_usuarios.html', context)

def detalle_usuario(request, usuario_id):
    # Obtener el usuario por ID o devolver un error 404 si no existe
    usuario = get_object_or_404(Usuario, id=usuario_id)
    
    context = {
        'usuario': usuario,
        'nombre_completo': f"{usuario.nombres} {usuario.apellidos}",
        'correo': usuario.correo,
        'celular': usuario.celular,
        'direccion': usuario.direccion,
        'rol': usuario.rol.nombre if usuario.rol else "Sin rol asignado",
    }
    return render(request, 'veterinary_users/detalle_usuario.html', context)