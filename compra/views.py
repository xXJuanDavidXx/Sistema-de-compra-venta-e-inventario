from django.shortcuts import render, redirect
from .models import Compra, DetallesDeCompra
from .forms import DetallesCompra

def compra(request):
    if request.method == 'POST':
        formset = DetallesCompra(request.POST)
        if formset.is_valid():
            compra = Compra.objects.create(usuario=request.user)
            for form in formset:
                detalle = form.save(commit=False)
                detalle.compra = compra  # Asociar la compra a cada detalle
                detalle.save()
            return redirect('compra_exitosa')  # Redirige a una página de éxito o resumen
    else:
        formset = DetallesCompra()

    return render(request, 'compra.html', {'form': formset})


