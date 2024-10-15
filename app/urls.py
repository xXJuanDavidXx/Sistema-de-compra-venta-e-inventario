from django.urls import path
from .views import AgregarProducto,ListarProductos

urlpatterns = [
        path('', ListarProductos.as_view(), name="lista"),
        path('Agregar/', AgregarProducto.as_view(), name="agregar"),
        
        ]

#Integrar vistas con url.
