from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from app.models import Producto
from .models import Compra, DetalleProducto



#ENTENDER Y TERMINAR
def agregar_a_compra(request, producto_id): #Le pasamos el id del producto desde la url.
    producto = get_object_or_404(Producto, id=producto_id)#busca el producto por id, si no lo encuentra, devuelve un 404

    cantidad = int(request.POST.get('cantidad',1)) #Recibimos la cantidad desde el formulario, si no se proporciona, se asume 1.

    # Obtener la compra activa del usuario o crear una nueva si no existe.
    compra, created = Compra.objects.get_or_create(usuario=request.user) #Con el id del usuario
    
    # Verificar si ya existe un detalle de compra para el producto
    detalle_producto, detalle_created = DetalleProducto.objects.get_or_create(
        compra=compra, #Obtiene a partir de la compra.
        producto=producto, #y a partir del producto. Ambos definidos arriba.
        defaults={'cantidad': cantidad } #Si no existe, se crea con la cantidad y el precio unitario del producto.
    )

    # Si ya existe, aumentar la cantidad
    if not detalle_created:
        detalle_producto.cantidad += cantidad
        detalle_producto.save()

    # Actualizar el total de la compra
    compra.actualizar_total()

    return redirect('lista')