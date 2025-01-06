from django.urls import path
from . import views

urlpatterns = [
    path('reporte_compras/', views.reporte_compras, name='reporte_compras'),
    path('reporte_ganancias/', views.reporte_ganancias, name='reporte_ganancias'),
    path('facturas/', views.facturas, name='facturas'),
    path('agregar_factura/', views.agregar_factura, name='agregar_factura'),
    path('reporte_diario/', views.reporte_diario, name='reporte_diario'),
    path('reporte_mensual/', views.reporte_mensual, name='reporte_mensual'),
    path('reporte_anual/', views.reporte_anual, name='reporte_anual'),
    path('Over/',views.actualizar_mes, name="over"), 
    path('diarios/', views.buscar_diario, name='buscar_diario'),
]

