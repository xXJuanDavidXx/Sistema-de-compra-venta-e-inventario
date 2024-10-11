from django.db import models   
from app.models import Producto #Se debe importar para los detalles de la orden.
from django.contrib.auth.models import User

# Create your models here.     

class Compra(models.Model):     
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #Si el usuario desaparece se borra la orden 
    order_date = models.DateTimeField(auto_now_add=True) #Se crea con la fecha actual
  
    #Le estamos agregando un formato a la forma en la que se va representar en el admin.
    def __str__(self):         
        return f"compra registrada. {self.id} - {self.order_date}"



#En esta clase se guardan todos los items de la orden.
class DetallesDeCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE) #LLave foranea de Order
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT) #Llave foranea de la clase products de la app principal (se importa) y en on_delete Protect para que no se borren los productos que ya estan en una orden 
    cantidad = models.IntegerField() #Para la cantidad de productos elegida.


    def __str__(self) -> str:
        return f"{self.compra} - {self.producto}"



