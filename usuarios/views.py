from .custom_claims import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import CategoriaModel
from .serializer import CategoriaSerializer
from .permissions import SoloMozos


class CategoriaApiView(ListCreateAPIView):
    # secuencia de permisos > el primer permiso se debe de cumplir para continuar con el segundo permiso y asi sucesivamente, si alguno falla (retorna False) entonces todo termina
    permission_classes = [IsAuthenticated, SoloMozos]
    # al utilizar una vista generica que ya no es necesario definir el comportamiento para cuando sea get o post
    # queryset > el comando que utilizara para llamar a la informacion de nuestra base de datos
    # SELECT * FROM categoria;
    queryset = CategoriaModel.objects.all()
    # serializer_class > se define una clase que se encargara de convertir y transformar la informacion que viene desde el cliente y la informacion que enviamos hacia el cliente en dato legibles
    serializer_class = CategoriaSerializer


# usuarios/views.py


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
