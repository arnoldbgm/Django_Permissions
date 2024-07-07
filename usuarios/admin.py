from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User  # Asegúrate de importar tu modelo User

# Define una clase de administrador personalizada si deseas personalizar la vista del admin
class CustomUserAdmin(UserAdmin):
    # Define los campos que quieres mostrar en la lista de usuarios
    list_display = ('username', 'email', 'tipoUsuario', 'is_staff', 'is_active')

# Registra el modelo User con el admin personalizado
admin.site.register(User, CustomUserAdmin)
