from rest_framework import serializers
from .models import CategoriaModel


class CategoriaSerializer(serializers.ModelSerializer):
    # cuando utilizamos un serializador basandonos en un modelo se declara la clase Meta
    class Meta:
        # este se encargara de mapear todos los atributos del modelo para hacer concordar el tipo de dato y sus especificaciones
        model = CategoriaModel
        # fields > sirve para indicar que columnas de esa tabla queremos trabajar, si queremos todas las columnas entonces definiremos el valor de '__all__' caso contrario lo podremos manejar en un arreglo con los nombre de las columnas
        fields = '__all__'

# usuarios/custom_claims.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['tipoUsuario'] = user.tipoUsuario

        return token
