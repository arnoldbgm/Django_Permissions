from django.urls import path
from .views import CategoriaApiView, MyTokenObtainPairView

urlpatterns = [
    path('categorias/', CategoriaApiView.as_view()),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
