from django.urls import path
from .views import AgregarProducto, ListarProductos, buscar_producto, Modificar_producto, modificar_producto

urlpatterns = [
        path('', ListarProductos.as_view(), name="lista"),
        path('Agregar/', AgregarProducto.as_view(), name="agregar"),
        path('buscar/', buscar_producto, name="buscar_producto"),
        path('lista/', Modificar_producto.as_view(), name="modificar_producto"),
        path('producto_a_modificar/<int:pk>/', modificar_producto, name="producto_a_modificar"),
        ]

#Integrar vistas con url.
