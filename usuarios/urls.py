from django.urls import path
from .views import CrearUsuario, LoginUsuario

urlpatterns = [
    path('crear_usuario/', CrearUsuario.as_view(), name='crear_usuario'),
    path('login/', LoginUsuario.as_view(), name='login'),

        ]


