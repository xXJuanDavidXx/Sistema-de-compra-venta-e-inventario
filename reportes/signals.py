from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Factura, Reporte, Reporte_anual, Reporte_mensual
from compra.models import Compra
from django.utils import timezone

@receiver(post_save, sender=Factura)
def actualizar_reporte_factura(sender, instance, created, **kwargs):
    if created:  # Solo si se crea una nueva factura
        fecha_actual = timezone.now().date()  # Obtener la fecha de hoy
        reporte, created = Reporte.objects.get_or_create(fecha=fecha_actual)  # Obtener o crear el reporte de hoy
        reporte.actualizar_ganancias()  # Actualizar las ganancias del reporte diario

@receiver(post_save, sender=Reporte)
def crear_reportes_mensuales_y_anuales(sender, instance, created, **kwargs):
    print("Se ha creado un nuevo reporte diario.")  # Agregado para depuración
    fecha_actual = timezone.now()  # Obtener la fecha y hora actual
    mes = fecha_actual.month  # Obtener el mes actual
    año = fecha_actual.year    # Obtener el año actual

    # Crear o actualizar el reporte mensual
    reporte_mensual, _ = Reporte_mensual.objects.get_or_create(mes=timezone.datetime(año, mes, 1))  # Usar el primer día del mes
    reporte_mensual.actualizar_ganancias()  # Actualizar ganancias independientemente de si fue creado o no

    # Crear o actualizar el reporte anual
    reporte_anual, _ = Reporte_anual.objects.get_or_create(año=año)  # Usar solo el año
    reporte_anual.actualizar_ganancias()  # Actualizar ganancias independientemente de si fue creado o no
