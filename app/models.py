from django.db import models

# Registro de productos

class Producto(models.Model):
    nombre = models.TextField(max_length = 200)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    porcentaje_ganancia = models.DecimalField(max_digits=5, decimal_places=2)
    precio_final = models.DecimalField(max_digits=10, decimal_places=2, editable=False)#El precio final se calcula con el precio original y el porcentaje por lo tanto no es editable
    stock = models.IntegerField()

    def save(self, *args, **kwargs): #Aqui vamos a calcular el precio original por el porcentaje
        #Calcular el precio final
        if self.precio_base and self.porcentaje_ganancia:
            self.precio_sin_redondear = self.precio_base + (self.precio_base * (self.porcentaje_ganancia/100))
            self.precio_final = (self.precio_sin_redondear + 49) // 50 * 50 #Redondeo al 50 mas cercano.
        else:
            self.precio_final = 0
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.nombre} - {self.precio_final} - {self.stock}"










