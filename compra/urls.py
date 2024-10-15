from django.urls import path
from .views import agregar_a_compra

urlpatterns = [
    path('<int:producto_id>/', agregar_a_compra, name="detalle_compra"),
        ]

