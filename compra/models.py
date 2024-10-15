from django.db import models   
from app.models import Producto #Se debe importar para los detalles de la orden.
from django.contrib.auth.models import User

# Create your models here.     

class Compra(models.Model):     
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #La relación ForeignKey indica que cada compra está asociada a un solo usuario, pero un usuario puede tener varias compras.
    order_date = models.DateTimeField(auto_now_add=True) #Se crea con la fecha actual
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
  
    #Le estamos agregando un formato a la forma en la que se va representar en el admin.
    def __str__(self):         
        return f"Compra {self.id} - {self.order_date}" 

    def actualizar_total(self): #Este método suma el total de los detalles de la compra (los productos y sus cantidades) y actualiza el campo total.
        self.total = sum(detalle.subtotal for detalle in self.detalleproducto_set.all())#self.detallesdecompra_set.all() accede a todos los objetos relacionados con la compra a través de la relación ForeignKey de DetallesDeCompra. Luego, calcula el subtotal para cada detalle y lo suma.
        self.save()

#En esta clase se guardan todos los items de la orden.
class DetalleProducto(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Detalle de compra {self.id} - {self.compra}"
    
    @property
    def subtotal(self):
        return self.cantidad * self.producto.precio_final
