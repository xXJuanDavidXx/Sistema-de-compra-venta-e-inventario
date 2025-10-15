from django import forms
from .models import Factura

class AgregarFactura(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['total']


class FiltroFechaForm(forms.Form):
    fecha_inicio = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label='Fecha Inicio'
    )
    fecha_fin = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label='Fecha Fin'
    )


class ReporteAnualFiltroForm(forms.Form):
    anio_inicio = forms.IntegerField(
        required=False,
        label="Año Inicio",
        widget=forms.NumberInput(attrs={'placeholder': 'Ej: 2020'})
    )
    anio_fin = forms.IntegerField(
        required=False,
        label="Año Fin",
        widget=forms.NumberInput(attrs={'placeholder': 'Ej: 2023'})
    )
