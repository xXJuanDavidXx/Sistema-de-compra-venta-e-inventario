from django.shortcuts import render, redirect
from compra.models import Compra
from .models import Reporte, Factura, ReporteMensual, ReporteAnual
from .forms import AgregarFactura, FiltroFechaForm, ReporteAnualFiltroForm
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
    form = FiltroFechaForm(request.GET or None)
    reportes = Reporte.objects.all().order_by("-id")
    return render(request, 'reportes/diario.html', {
        'form': form,
        'reportes': reportes,
        'actual': 'reporte_ganancias'
    })


def buscar_diario(request):
    form = FiltroFechaForm(request.GET or None)
    reportes = Reporte.objects.all().order_by("-fecha")
    
    if form.is_valid():
        fecha_inicio = form.cleaned_data.get('fecha_inicio')
        fecha_fin = form.cleaned_data.get('fecha_fin')

        if fecha_inicio:
            reportes = reportes.filter(fecha__gte=fecha_inicio)
        if fecha_fin:
            reportes = reportes.filter(fecha__lte=fecha_fin)


    return render(request, 'reportes/resultados/resultados_dias.html', {
        'form': form,
        'reportes': reportes,
        'actual': 'reporte_ganancias'
        })





#Mensuales
def reporte_mensual(request):
    form = FiltroFechaForm(request.GET or None)
    return render(request, 'reportes/mensual.html', {
        'form': form,
        'mensual': ReporteMensual.objects.all().order_by("-id"),
        'actual':'reporte_ganancias'
        })

def buscar_mensual(request):
    form = FiltroFechaForm(request.GET or None)
    reportes = ReporteMensual.objects.all().order_by("-mes")
    
    if form.is_valid():
        fecha_inicio = form.cleaned_data.get('fecha_inicio')
        fecha_fin = form.cleaned_data.get('fecha_fin')

        if fecha_inicio:
            reportes = reportes.filter(mes__gte=fecha_inicio)
        if fecha_fin:
            reportes = reportes.filter(mes__lte=fecha_fin)


    return render(request, 'reportes/resultados/resultados_meses.html', {
        'form': form,
        'mensual': reportes,
        'actual': 'reporte_ganancias'
        })



#Anuales
def reporte_anual(request):
    form = ReporteAnualFiltroForm(request.GET or None)
    return render(request, 'reportes/anual.html', {
        'form':form,
        'anual': ReporteAnual.objects.all().order_by("-id"),
        'actual':'reporte_ganancias'
        })


def buscar_anual(request):
    form = ReporteAnualFiltroForm(request.GET or None)
    reportes = ReporteAnual.objects.all()

    if form.is_valid():
        anio_inicio = form.cleaned_data.get('anio_inicio')
        anio_fin = form.cleaned_data.get('anio_fin')

        if anio_inicio:
            reportes = reportes.filter(anio__gte=anio_inicio)  # >= año inicio
        if anio_fin:
            reportes = reportes.filter(anio__lte=anio_fin)    # <= año fin

    return render(request, 'reportes/resultados/resultados_años.html', {
        'form': form,
        'anual': reportes,
        'actual': 'reporte_ganancias'
    })



def actualizar_mes(request):
    hoy = date.today()
    primer_dia_mes = hoy.replace(day=1)
    reporte_mensual, creado = ReporteMensual.objects.get_or_create(mes=primer_dia_mes)
    reporte_mensual.actualizar_datos_mensuales()
    return redirect('reporte_diario')




