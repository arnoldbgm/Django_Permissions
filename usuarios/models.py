from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    tipoUsuario = models.CharField(max_length=40, choices=[
        ('ADMIN', 'Administrador'),
        ('MOZO', 'Mozo'),
        ('CLIENTE', 'Cliente')
    ], default='CLIENTE')

    REQUIRED_FIELDS = ['tipoUsuario']
