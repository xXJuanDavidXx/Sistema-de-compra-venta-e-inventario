from django.urls import path
from .views import AgregarProducto, ListarProductos, buscar_producto

urlpatterns = [
        path('', ListarProductos.as_view(), name="lista"),
        path('Agregar/', AgregarProducto.as_view(), name="agregar"),
        path('buscar/', buscar_producto, name="buscar_producto"),
        ]

#Integrar vistas con url.
