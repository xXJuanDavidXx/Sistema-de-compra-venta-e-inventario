from django.urls import path
from .views import agregar_a_compra, eliminar_del_carrito, cerrar_compra

urlpatterns = [
    path('<int:producto_id>/', agregar_a_compra, name="detalle_compra"),
    path('venta/', cerrar_compra, name="venta"),
    path('eliminar/<int:producto_id>/', eliminar_del_carrito, name="eliminar_del_carrito"),
        ]

