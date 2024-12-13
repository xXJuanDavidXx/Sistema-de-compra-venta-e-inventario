from django.db import models   
from app.models import Producto #Se debe importar para los detalles de la orden.
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.     

class Compra(models.Model):     
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación de compra con un usuario; un usuario puede tener múltiples compras.
    order_date = models.DateTimeField(auto_now_add=True)  # Fecha de creación de la compra.
    total = models.DecimalField(max_digits=10, decimal_places=0, default=0)  # Total de la compra.
    estado = models.BooleanField(default=True)  # Estado de la compra: True si está activa, False si está cerrada.

    def __str__(self):         
        return f"Compra {self.id} - {self.order_date}" 

    def actualizar_total(self):  # Suma el total de los detalles de la compra y actualiza el campo total.
        self.total = sum(detalle.subtotal for detalle in self.detalles.all())  # Calcula el subtotal de todos los detalles.
        self.save()

    def cerrar_compra(self):  # Finaliza la compra actual.
        self.estado = False
        self.save()
        
        # Actualiza el reporte del día actual
        from reportes.models import Reporte  # Importación local para evitar conflictos.
        fecha_actual = timezone.now().date()  # Obtiene la fecha de hoy.
        reporte, created = Reporte.objects.get_or_create(fecha=fecha_actual)  # Obtiene o crea el reporte de hoy.
        reporte.actualizar_ganancias()  # Actualiza las ganancias del día.

class DetalleProducto(models.Model):
    """
    Clase que representa los ítems de la orden.
    """
    compra = models.ForeignKey(Compra, related_name='detalles', on_delete=models.CASCADE)  # Relación con la compra.
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)  # Relación con el producto.
    cantidad = models.PositiveIntegerField()  # Cantidad del producto.
    
    def __str__(self):
        return f"Detalle de compra {self.id} - {self.compra}"
    
    @property  # Permite acceder a este método como un atributo, sin necesidad de llamarlo como una función.
    def subtotal(self):  # Calcula el subtotal de cada producto en función de su cantidad.
        # Multiplica la cantidad del producto por su precio final para obtener el subtotal.
        return self.cantidad * self.producto.precio_final
