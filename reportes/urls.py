from django.urls import path
from .views import reporte_compras, reporte_ganancias, facturas, agregar_factura

urlpatterns = [
    path('reporte_compras/', reporte_compras, name='reporte_compras'),
    path('reporte_ganancias/', reporte_ganancias, name='reporte_ganancias'),
    path('facturas/', facturas, name='facturas'),
    path('agregar_factura/', agregar_factura, name='agregar_factura'),
]

