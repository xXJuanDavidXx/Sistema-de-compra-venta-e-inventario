from django.contrib import admin
from .models import DetalleProducto, Compra

# Register your models here.

class DetalleProductoAdmin(admin.TabularInline):
    model = DetalleProducto
    extra = 1

class CompraAdmin(admin.ModelAdmin):
    model = Compra
    inlines = [DetalleProductoAdmin]

admin.site.register(Compra, CompraAdmin)

