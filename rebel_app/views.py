from django.db.models.fields.files import ImageField
from rebel_app.models import Receta
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RecetaForm
from .forms import CustomUserForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
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

def login_user(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'temp_app:logout')

def register(request):
    data= {
        'form':CustomUserForm()
    }

    if request.method == 'POST': 
        formulario = CustomUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #autenticar al usuario y redirigirlo al inicio           
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            #messages.success(request,"Te has registrado con exito!")           
            return redirect(to='temp_app:home')
        data["form"] = formulario
    return render(request, 'register.html', data)


def somos(request):
    return render(request, 'somos.html')

#gabo
def agregar_receta(request):
    data = {
        'form': RecetaForm()
    }
    
    if request.method == 'POST':
        formulario = RecetaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Receta Agregada correctamente"
            return redirect(to='temp_app:listar_receta')
        else:
            data["form"] = formulario
    
    return render(request, 'receta/agregar.html', data)

def listar_receta(request):
    recetas = Receta.objects.all()
    
    data ={
        'recetas': recetas
    }
    return render(request, 'receta/listar.html', data)

def modificar_receta(request, id):
    receta = get_object_or_404(Receta, id=id)
    data = {
        'form': RecetaForm(instance=receta)
    }
    if request.method == 'POST':
        formulario = RecetaForm(data=request.POST, instance=receta, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='temp_app:listar_receta')
        data["form"] = formulario
        
    return render(request, 'receta/modificar.html', data)

def eliminar_receta(request, id):
    receta = get_object_or_404(Receta, id=id)
    receta.delete()
    return redirect(to="temp_app:listar_receta")



#luis
def pedidos(request):
    return render(request, 'pedidos.html')

#def producto_list(request):
#   productos = Producto.objects.all()
 #   return render(request,'pedidos.html', {'productos': productos})

class ListarProductos(ListView):
    template_name = "pedidos.html"
    #context_object_name = 'ListaProd'
    model = producto


class ProductoCreateView(CreateView):
    template_name = "agrega_prod.html"
    model = producto
    fields = ['name','tipo_prod','description','price','imagen']
    success_url = reverse_lazy('temp_app:agregar')


class ProductoUpdateView(UpdateView):
    template_name = "modificar_prod.html"
    model = producto
    fields = ('__all__')
    
    success_url = reverse_lazy('temp_app:pedido')

  #  def post(self,request, *args, **kwargs):
   #     self.object = self.get_object()
    #    print('************METOD POST*************')
     #   print(request.POST)
      #  print(request.POST ['name'])
       # return super().post(request, *args, **kwargs)

class ProductoDeleteView(DeleteView):
    template_name = "pedidos.html"
    model = producto

    success_url = reverse_lazy('temp_app:eliminar')
    

    

