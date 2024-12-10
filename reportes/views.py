from django.shortcuts import render, redirect
from compra.models import Compra
from .models import Reporte, Factura
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
    compras = Compra.objects.all()
    return render(request, 'reporte_compras.html', {'compras': compras})


def reporte_facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'reporte_facturas.html', {'facturas': facturas})



#Mostrar el reporte de ganancias por día
def reporte_ganancias(request):
    reportes = Reporte.objects.all()
    return render(request, 'reporte_ganancias.html', {'reportes': reportes})