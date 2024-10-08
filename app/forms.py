from django import forms
from .models import Producto

class Agregar(forms.Form):
    nombre = forms.CharField(max_length=200, label="Nombre")
    precio_base = forms.DecimalField(max_digits=5, decimal_places=2, label="Precio base")
    porcentaje_ganancia = forms.DecimalField(max_digits=5, decimal_places=2, label="Porcentaje de ganancia")
    stock = forms.IntegerField(label="Cantidad")

    
