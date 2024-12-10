from django import forms
from .models import Factura

class AgregarFactura(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['total']

