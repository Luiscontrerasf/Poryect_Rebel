from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)
from django.http import request
from .models import producto


# Create your views here.

def home(request):
    return render(request, 'index2.html')

def torta(request):
    return render(request, 'Tortas.html')

def salado(request):
    return render(request, 'Salados.html')

def dulce(request):
    return render(request, 'Dulces.html')

def contacto(request):
    return render(request, 'contacto.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def somos(request):
    return render(request, 'somos.html')

def pedidos(request):
    return render(request, 'pedidos.html')

#def producto_list(request):
#   productos = Producto.objects.all()
 #   return render(request,'pedidos.html', {'productos': productos})

class ListarProductos(ListView):
    template_name = 'pedidos.html'
    #context_object_name = 'ListaProd'
    model = producto


class ProductoCreateView(CreateView):
    template_name = "agrega_prod.html"
    model = producto
    fields = ('__all__')
    success_url = reverse_lazy('temp_app:agregar')


class ProductoUpdateView(UpdateView):
    template_name = "modificar_prod.html"
    model = producto
    fields = ('__all__')
    
    success_url = reverse_lazy('temp_app:modificar')

  #  def post(self,request, *args, **kwargs):
   #     self.object = self.get_object()
    #    print('************METOD POST*************')
     #   print(request.POST)
      #  print(request.POST ['name'])
       # return super().post(request, *args, **kwargs)
    

