from rebel_app.models import Receta
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RecetaForm

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

def agregar_receta(request):
    data = {
        'form': RecetaForm()
    }
    
    if request.method == 'POST':
        formulario = RecetaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Receta Agregada correctamente"
            return redirect(to='listar_receta')
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
            return redirect(to='listar_receta')
        data["form"] = formulario
        
    return render(request, 'receta/modificar.html', data)

def eliminar_receta(request, id):
    receta = get_object_or_404(Receta, id=id)
    receta.delete()
    return redirect(to="listar_receta")

