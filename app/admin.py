from django.contrib import admin
from .models import Producto

# Register your models here.

class VerProducto(admin.ModelAdmin):
    model = Producto
    list_display = ['nombre', 'precio_final','stock']
    search_fields = ['nombre']

admin.site.register(Producto, VerProducto)

