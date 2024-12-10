from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Factura, Reporte
from compra.models import Compra
from django.utils import timezone

@receiver(post_save, sender=Factura)
def actualizar_reporte_factura(sender, instance, created, **kwargs):
    if created:  # Solo si se crea una nueva factura
        fecha_actual = timezone.now().date()  # Obtener la fecha de hoy
        reporte, created = Reporte.objects.get_or_create(fecha=fecha_actual)  # Obtener o crear el reporte de hoy
        reporte.actualizar_ganancias()  # Actualizar las ganancias del día

@receiver(pre_save, sender=Compra)
def actualizar_reporte_compra(sender, instance, **kwargs):
    # Detectar si el estado cambió de True a False
    if instance.pk:  # Verifica si la compra ya existe en la base de datos (no es nueva)
        compra_anterior = Compra.objects.get(pk=instance.pk)
        if compra_anterior.estado == True and instance.estado == False:
            # Si el estado cambió de True a False, actualizamos el reporte
            fecha_actual = timezone.now().date()  # Obtener la fecha de hoy
            reporte, created = Reporte.objects.get_or_create(fecha=fecha_actual)  # Obtener o crear el reporte de hoy
            reporte.actualizar_ganancias()  # Actualizar las ganancias del día
