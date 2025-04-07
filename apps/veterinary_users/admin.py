from django.contrib import admin
from .models import Perfil, Usuario, UserAccount, UserActivity, UserMessage
# Register your models here.


admin.site.register(Perfil)
admin.site.register(Usuario)
admin.site.register(UserAccount)
admin.site.register(UserActivity)
admin.site.register(UserMessage)