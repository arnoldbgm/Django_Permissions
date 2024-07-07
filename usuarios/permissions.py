from rest_framework.permissions import BasePermission
from .models import User


class SoloMozos(BasePermission):
    message = 'Solamente los mozos pueden realizar esta accion'

    def has_permission(self, request, view):
        usuario:User = request.user
        if usuario.tipoUsuario == 'MOZO':
            return True
        else:
            return False
