from django.shortcuts import render, redirect
from compra.models import Compra
from .models import Reporte, Factura, Reporte_mensual, Reporte_anual
from .forms import AgregarFactura

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
    return render(request, 'facturas.html', {'facturas': facturas})


def reporte_compras(request):
    compras = Compra.objects.all().order_by("-id")
    return render(request, 'reporte_compras.html', {'compras': compras})


#Mostrar el reporte de ganancias por día
def reporte_ganancias(request):
    diarios = Reporte.objects.all()
    mensual = Reporte_mensual.objects.all()
    aunual = Reporte_anual.objects.all()
    
    return render(request, 'reporte_ganancias.html', {
        'reportes': diarios,
        'mensual': mensual,
        'anual': aunual 
          })











