from django.urls import path
from .views import agregar_a_compra, ver_compra, eliminar_del_carrito

urlpatterns = [
    path('<int:producto_id>/', agregar_a_compra, name="detalle_compra"),
    path('venta/', ver_compra, name="venta"),
    path('eliminar/<int:producto_id>/', eliminar_del_carrito, name="eliminar_del_carrito"),
        ]

