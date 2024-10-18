from django.shortcuts import get_object_or_404, redirect
from app.models import Producto
from .models import Compra, DetalleProducto
from django.contrib import messages


def agregar_a_compra(request, producto_id):
    """
    Agrega un producto al carrito.

     Recibe el id del producto desde la url y la cantidad desde el formulario.
    """
    producto = get_object_or_404(Producto, id=producto_id)#busca el producto por id, si no lo encuentra, devuelve un 404

    cantidad = int(request.POST.get('cantidad',1)) #Recibimos la cantidad desde el formulario, si no se proporciona, se asume 1.

    # Obtener la compra activa del usuario o crear una nueva si no existe.
    compra, created = Compra.objects.get_or_create(usuario=request.user, estado=True) #Con el id del usuario y estado true, obtiene la compra activa.
    
    # Verificar si ya existe un detalle de compra para el producto si no lo crea.
    detalle_producto, detalle_created = DetalleProducto.objects.get_or_create(
        compra=compra, #Obtiene a partir de la compra.
        producto=producto, #y a partir del producto. Ambos definidos arriba.
        defaults={'cantidad': 0} #Si no existe, se crea con la cantidad primero en 0.
    )

    # Calculamos la nueva cantidad total en el carrito
    nueva_cantidad_total = detalle_producto.cantidad + cantidad

    # Verificamos si la nueva cantidad total excede el stock disponible
    if nueva_cantidad_total > producto.stock:
        messages.error(request, 'La cantidad solicitada excede el stock disponible')
        return redirect('lista')

    # Si hay suficiente stock, actualizamos la cantidad
    detalle_producto.cantidad = nueva_cantidad_total
    detalle_producto.save()

    # Actualizar el total de la compra
    compra.actualizar_total()

    messages.success(request, 'Producto agregado al carrito correctamente')
    return redirect('lista')


#CREAR UNA VISTA PARA MODIFICAR LA CANTIDAD DE UN PRODUCTO EN EL CARRITO


#def ver_compra(request):
#    compra = Compra.objects.get(usuario=request.user, estado=True)
#    detalles = DetalleProducto.objects.filter(compra=compra)
#    return render(request, 'compra.html', {'compra': compra, 'detalles': detalles})

def eliminar_del_carrito(request, producto_id):
    """
    Elimina un producto del carrito.
    Recibe el id del producto desde la url.
    """
    producto = get_object_or_404(Producto, id=producto_id) #Busca el producto por id.
    compra = Compra.objects.get(usuario=request.user, estado=True) #Busca la compra del usuario.
    detalle_producto = DetalleProducto.objects.get(compra=compra, producto=producto) #Busca el detalle del producto en la compra.
    detalle_producto.delete() #Elimina el detalle del producto.
    compra.actualizar_total() #Actualiza el total de la compra.
    return redirect('lista') #Redirige a la lista de productos.


def cerrar_compra(request):
    """
    Cierra la compra actual y actualiza el stock de los productos.
    """    
    try: #Probamos a obtener la compra activa del usuario.
        compra = Compra.objects.get(usuario=request.user, estado=True)#Obtenemos la compra activa del usuario.
        detalles = DetalleProducto.objects.filter(compra=compra)#Obtenemos los detalles asociados a la compra.
        for detalle in detalles:#Por cada detalle, se resta la cantidad del producto del stock.
            producto = detalle.producto
            producto.stock -= detalle.cantidad
            producto.save()

        compra.cerrar_compra()#Cierramos la compra actual con el metodo definido.
        return redirect('lista')
    except Compra.DoesNotExist: #Si no existe se manda un mensaje de error y se redirige a la lista de productos.
        messages.error(request, 'No hay una compra activa')
        return redirect('lista')





