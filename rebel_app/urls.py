from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('Tortas.html', views.torta, name="torta"),
    path('Dulces.html', views.dulce, name="dulce"),
    path('Salados.html', views.salado, name="salado"),
]