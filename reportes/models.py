from django.db import models
from compra.models import Compra
from django.utils import timezone
from datetime import timedelta
from dateutil.relativedelta import relativedelta

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
        self.ingresos = sum(Compra.objects.filter(estado=False, order_date__date=timezone.now().date()).values_list('total', flat=True)) # AL devolver una lista se suman todos los registros de la venta de un dia (REVISAR)
        self.gastos = sum(Factura.objects.filter(fecha=timezone.now().date()).values_list('total', flat=True))
        self.ganancia = self.ingresos - self.gastos
        self.save()



class ReporteMensual(models.Model):
    """El modelo de reporte mensual que resume el estado de ganancias de la empresa por mes"""
    mes = models.DateField(unique=True)  # Representa el primer día del mes
    ingresos = models.DecimalField(max_digits=15, decimal_places=0, default=0)  # Ingresos totales del mes
    gastos = models.DecimalField(max_digits=15, decimal_places=0, default=0)  # Gastos totales del mes
    ganancia = models.DecimalField(max_digits=15, decimal_places=0, default=0)  # Ganancia total del mes

    def actualizar_datos_mensuales(self):
        """Actualiza los ingresos, gastos y ganancia del mes"""
        inicio_mes = self.mes.replace(day=1)
        fin_mes = (inicio_mes + relativedelta(months=1)) - timedelta(days=1) #suma un mes y resta un dia para obtener el ultimo dia del mes.

        # Sumar ingresos, gastos y ganancias de los reportes diarios del mes
        reportes_diarios = Reporte.objects.filter(fecha__range=[inicio_mes, fin_mes])
        self.ingresos = sum(reportes_diarios.values_list('ingresos', flat=True))
        self.gastos = sum(reportes_diarios.values_list('gastos', flat=True))
        self.ganancia = self.ingresos - self.gastos
        self.save()


class ReporteAnual(models.Model):
    """El modelo de reporte anual que resume el estado de ganancias de la empresa por año"""
    anio = models.IntegerField(unique=True)  # Año del reporte
    ingresos = models.DecimalField(max_digits=20, decimal_places=0, default=0)  # Ingresos totales del año
    gastos = models.DecimalField(max_digits=20, decimal_places=0, default=0)  # Gastos totales del año
    ganancia = models.DecimalField(max_digits=20, decimal_places=0, default=0)  # Ganancia total del año

    def actualizar_datos_anuales(self):
        """Actualiza los ingresos, gastos y ganancia del año"""
        reportes_mensuales = ReporteMensual.objects.filter(mes__year=self.anio)
        self.ingresos = sum(reportes_mensuales.values_list('ingresos', flat=True))
        self.gastos = sum(reportes_mensuales.values_list('gastos', flat=True))
        self.ganancia = self.ingresos - self.gastos
        self.save()



