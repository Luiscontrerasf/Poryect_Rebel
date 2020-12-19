from django.shortcuts import render

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

