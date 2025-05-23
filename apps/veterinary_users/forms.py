from django import forms
from .models import Usuario, UserAccount, Perfil

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombres', 'apellidos', 'tipodocumento', 'numerodocumento',
            'correo', 'celular', 'direccion', 'rol'
        ]

class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['username', 'contrasena', 'activo']
        widgets = {
            'contrasena': forms.PasswordInput(),
        }

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nombre', 'descripcion']