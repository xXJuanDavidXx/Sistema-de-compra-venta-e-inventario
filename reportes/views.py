from django.shortcuts import render, redirect
from compra.models import Compra
from .models import Reporte, Factura, ReporteMensual, ReporteAnual
from .forms import AgregarFactura
from datetime import date
from dateutil.relativedelta import relativedelta
from django.urls import reverse_lazy
from django.http import HttpResponse


# Create your views here.

def agregar_factura(request):
    if request.method == 'POST':
        form = AgregarFactura(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facturas')
    else:
        form = AgregarFactura()
    return render(request, 'agregar_factura.html', {'form': form})


def facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'facturas.html', {'facturas': facturas, 'actual':'facturas'})


def reporte_compras(request):
    compras = Compra.objects.all().order_by("-id")
    return render(request, 'reporte_compras.html', {'compras': compras, 'actual':'reporte_compras'})


#Mostrar el reporte de ganancias por día
def reporte_ganancias(request):
    diarios = Reporte.objects.last()
    
    return render(request, 'reporte_ganancias.html', {
        'reportes': diarios,
        'actual':'reporte_ganancias'
          })


#Diarios
def reporte_diario(request):
    reportes = Reporte.objects.all().order_by("-id")
    return render(request, 'reportes/diario.html', {
        'reportes': reportes,
        'actual': 'reporte_ganancias'
    })


def buscar_diario(request):
    query = request.GET.get('q')
    reportes = Reporte.objects.filter(fecha__icontains=query)
    return render(request, 'reportes/resultados/resultados_dias.html', {
        'reportes': reportes,
        'actual': 'reporte_ganancias'
    })

#Mensuales
def reporte_mensual(request):
    return render(request, 'reportes/mensual.html', {
        'mensual': ReporteMensual.objects.all().order_by("-id"),
        'actual':'reporte_ganancias'
        })


#Anuales
def reporte_anual(request):
    return render(request, 'reportes/anual.html', {
        'anual': ReporteAnual.objects.all().order_by("-id"),
        'actual':'reporte_ganancias'
        })




def actualizar_mes(request):
    hoy = date.today()
    primer_dia_mes = hoy.replace(day=1)
    reporte_mensual, creado = ReporteMensual.objects.get_or_create(mes=primer_dia_mes)
    reporte_mensual.actualizar_datos_mensuales()
    return redirect('reporte_diario')




