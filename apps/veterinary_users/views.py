from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .forms import UsuarioForm, UserAccountForm, PerfilForm
from .models import Perfil, Usuario, UserAccount, UserMessage, UserActivity

def home_users(request):
    mensaje = ""
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        try:
            usuario = Usuario.objects.get(correo=correo)
            cuenta = UserAccount.objects.get(usuario=usuario)
            if cuenta.contrasena == contrasena:
                return redirect('dashboard', useraccount_id = cuenta.id)
            else:
                mensaje = "Contraseña incorrecta."
        except Usuario.DoesNotExist:
            mensaje = "Correo no registrado."
        except UserAccount.DoesNotExist:
            mensaje = "La cuenta de usuario no existe."
    return render(request, 'veterinary_users/home_users.html', {'mensaje': mensaje})

def registro_usuarios(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            return redirect('cuenta_usuarios', usuario_id = usuario.id)
    else:
        form = UsuarioForm()
    perfiles = Perfil.objects.all()
    return render(request, 'veterinary_users/registro_usuarios.html', {'form': form, 'perfiles': perfiles})

def cuenta_usuarios(request, usuario_id):
    usuario = get_object_or_404(Usuario, id = usuario_id)
    if request.method == 'POST':
        form = UserAccountForm(request.POST)
        if form.is_valid():
            cuenta = form.save(commit=False)
            cuenta.usuario = usuario
            cuenta.save()
            return redirect('dashboard', useraccount_id = cuenta.id)
    else:
        form = UserAccountForm()
    return render(request, 'veterinary_users/cuenta_usuarios.html', {'form': form, 'usuario_id': usuario.id})

def dashboard(request, useraccount_id):
    user_account = get_object_or_404(UserAccount, id=useraccount_id)
    usuario = user_account.usuario
    perfil = usuario.rol
    notificaciones = UserMessage.objects.filter(usuario=usuario).order_by('-fecha')[:5]
    roles = Perfil.objects.all()
    context = {
        'user_account': user_account,
        'usuario': usuario,
        'perfil': perfil,
        'notificaciones': notificaciones,
        'roles': roles,
    }
    return render(request, 'veterinary_users/dashboard.html', context)

def actualizar_usuarios(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    user_account = UserAccount.objects.get(usuario = usuario)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('dashboard', useraccount_id=user_account.id)
    else:
        form = UsuarioForm(instance=usuario)
    perfiles = Perfil.objects.all()
    return render(request, 'veterinary_users/actualizar_usuarios.html', {
        'form': form,
        'usuario': usuario,
        'perfiles': perfiles,
        'user_account': user_account, 
    })

def actualizar_contrasena(request, useraccount_id):
    user_account = get_object_or_404(UserAccount, id=useraccount_id)
    mensaje = ""
    if request.method == 'POST':
        contrasenavieja = request.POST.get('contrasenavieja')
        contrasenanueva = request.POST.get('contrasenanueva')
        contrasena = request.POST.get('contrasena')

        if contrasenavieja != user_account.contrasena:
            mensaje = "La contraseña actual no es correcta."
        elif contrasenanueva != contrasenanueva:
            mensaje = "La contraseña no coinciden."
        else:
            user_account.contrasena = contrasena
            user_account.save()
            return redirect('dashboard', useraccount_id=user_account.id)
    return render(request, 'veterinary_users/actualizar_contrasena.html', {
        'user_account': user_account,
        'mensaje': mensaje,
    })

def rol(request, useraccount_id):
    if request.method == 'POST':
        form = PerfilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard', useraccount_id=useraccount_id)
    else:
        form = PerfilForm()
    return render(request, 'veterinary_users/rol.html', {'form': form, 'useraccount_id': useraccount_id})

def editar_rol(request, rol_id, useraccount_id):
    perfil = get_object_or_404(Perfil, id=rol_id)
    mensaje = ""
    if request.method == 'POST':
        accion = request.POST.get('accion')
        if accion == 'actualizar':
            perfil.nombre = request.POST.get('nombre')
            perfil.descripcion = request.POST.get('descripcion')
            perfil.save()
            return redirect('dashboard', useraccount_id=useraccount_id)
        elif accion == 'eliminar':
            perfil.delete()
            return redirect('dashboard', useraccount_id=useraccount_id)
    return render(request, 'veterinary_users/a_e_rol.html', {
        'perfil': perfil,
        'mensaje': mensaje,
        'useraccount_id': useraccount_id
    })