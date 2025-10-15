from django import forms
from .models import DetallesDeCompra
from django.forms import modelformset_factory


class DetallesCompra(forms.ModelForm):
    class Meta:
        model = DetallesDeCompra
        fields = ['producto','cantidad']

