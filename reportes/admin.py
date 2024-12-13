from django.contrib import admin 
from . import models 

# Register your models here.

admin.site.register(models.Factura)
admin.site.register(models.Reporte)
admin.site.register(models.Reporte_mensual)
admin.site.register(models.Reporte_anual)