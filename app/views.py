from django.shortcuts import render
from django.views import generic
from .forms import Agregar
from django.urls import reverse_lazy
from .models import Producto


# Create your views here.


class AgregarProducto(generic.FormView):
    #FormView para administrar el formulrio.
    form_class = Agregar #El formulario
    template_name = "agregar.html" #La dirección del template
    success_url = reverse_lazy('lista') #La url donde vamos a redirigir al usuario



    def form_valid(self, form):
        """
    Sobree escribo el from_valid para poder manejar el inventario en la base de datos y la modificacion del precio.

        """
        nombre = form.cleaned_data['nombre'] #la data procesada por el formulario
        precio_base = form.cleaned_data['precio_base'] 
        porcentaje_ganancia = form.cleaned_data['porcentaje_ganancia']
        stock = form.cleaned_data['stock']
    
        producto, created = Producto.objects.get_or_create(nombre=nombre,
            defaults={
            'precio_base': precio_base,
            'porcentaje_ganancia': porcentaje_ganancia,
            'stock': stock
            #En el diccionario estan los datos que se van a guardar en la base de datos cuando created es verdadero, es decir, que el producto no existe.
            }
    ) #Si el producto existe created es falso y se guarda lo obtenido en producto, pero si no existe es verdadero y se crea en producto

        if not created: #Si created es falso, entonces
            producto.precio_base = precio_base
            producto.porcentaje_ganancia = porcentaje_ganancia
            #Guardamos el nuevo precio y el nuevo porcentaje

            producto.stock += stock
            #sumamos al stock la cantidad que se pase

            producto.save()
            #Guardamos el producto.
            mensaje = "Se catualizo un producto."
            
        else:
            #Si no, el producto ya se creo y se guardo por el metodo get_or_created
            mensaje = "Se creo un producto"


        
        return super().form_valid(form)



class ListarProductos(generic.ListView):
    #ListView para que se listen los productos desde el template tranquilamente.
    model = Producto
    context_object_name = 'productos'
    template_name = 'listaProductos.html'





    








