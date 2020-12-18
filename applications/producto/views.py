from django.shortcuts import render
from django.views.generic import (
    ListView
)
# Create your views here.
from .models import producto

class listaAllProducts(ListView):
    template_name = 'producto/list_all.html'
    model = producto