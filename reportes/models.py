from django.db import models
from compra.models import Compra
from django.utils import timezone

# Create your models here.

class Factura(models.Model):
    """El modelo factura que representa un gasto por registro"""
    total = models.DecimalField(max_digits=10, decimal_places=0) #El total de la factura
    fecha = models.DateField(auto_now_add=True) #La fecha de la factura

    def __str__(self):
        return f"Factura {self.id} - {self.fecha}"


class Reporte(models.Model):
    """El modelo reporte que representa el estado de ganancias de la empresa por día"""
    fecha = models.DateField(default=timezone.now, unique=True) #La fecha del reporte
    ingresos = models.DecimalField(max_digits=10, decimal_places=0, default=0) #Los ingresos de la empresa por día
    gastos = models.DecimalField(max_digits=10, decimal_places=0, default=0) #Los gastos de la empresa por día
    ganancia = models.DecimalField(max_digits=10, decimal_places=0, default=0) #La ganancia de la empresa por día

    def actualizar_ganancias(self):
        """Actualiza los ingresos, gastos y ganancia de la empresa por día"""
        self.ingresos = sum(Compra.objects.filter(estado=False, order_date__date=timezone.now().date()).values_list('total', flat=True))
        self.gastos = sum(Factura.objects.filter(fecha=timezone.now().date()).values_list('total', flat=True))
        self.ganancia = self.ingresos - self.gastos
        self.save()



### De aqui para abajo revisar.

class Reporte_mensual(models.Model):
    """El modelo reporte mensual que representa el estado de ganancias de la empresa por mes"""
    mes = models.DateField()  # La fecha del mes del reporte
    ingresos = models.DecimalField(max_digits=10, decimal_places=0, default=0)  # Los ingresos de la empresa por mes
    gastos = models.DecimalField(max_digits=10, decimal_places=0, default=0)  # Los gastos de la empresa por mes
    ganancia = models.DecimalField(max_digits=10, decimal_places=0, default=0)  # La ganancia de la empresa por mes

    def actualizar_ganancias(self):
        """Actualiza los ingresos, gastos y ganancia de la empresa por mes desde los reportes diarios"""
        self.ingresos = sum(Reporte.objects.filter(fecha__month=self.mes.month, fecha__year=self.mes.year).values_list('ingresos', flat=True))
        self.gastos = sum(Reporte.objects.filter(fecha__month=self.mes.month, fecha__year=self.mes.year).values_list('gastos', flat=True))
        self.ganancia = self.ingresos - self.gastos
        self.save()


class Reporte_anual(models.Model):
    """El modelo reporte anual que representa el estado de ganancias de la empresa por año"""
    año = models.DateField()  # La fecha del año del reporte
    ingresos = models.DecimalField(max_digits=10, decimal_places=0, default=0)  # Los ingresos de la empresa por año
    gastos = models.DecimalField(max_digits=10, decimal_places=0, default=0)  # Los gastos de la empresa por año
    ganancia = models.DecimalField(max_digits=10, decimal_places=0, default=0)  # La ganancia de la empresa por año

    def actualizar_ganancias(self):
        """Actualiza los ingresos, gastos y ganancia de la empresa por año desde los reportes mensuales"""
        self.ingresos = sum(Reporte_mensual.objects.filter(mes__year=self.año.year).values_list('ingresos', flat=True))
        self.gastos = sum(Reporte_mensual.objects.filter(mes__year=self.año.year).values_list('gastos', flat=True))
        self.ganancia = self.ingresos - self.gastos
        self.save()



