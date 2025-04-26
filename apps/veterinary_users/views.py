from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Usuario

def home_users(request):
    return render(request,'veterinary_users/home_users.html')

def lista_usuarios(request):
    
    usuarios = Usuario.objects.all()
    
    context = {
        'usuarios': usuarios,
        'total_usuarios': usuarios.count(),  
    }
    return render(request, 'veterinary_users/lista_usuarios.html', context)

def detalle_usuario(request, usuario_id):
    
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