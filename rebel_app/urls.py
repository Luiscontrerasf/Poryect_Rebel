#from django.contrib import admin
from django.urls import path
from . import views

app_name = "temp_app"

urlpatterns = [
    path('', views.home, name="home"),
    path('Tortas/', views.torta, name="torta"),
    path('Dulces.html', views.dulce, name="dulce"),
    path('Salados.html', views.salado, name="salado"),
    path('contacto/', views.contacto, name="contacto"),
    path('login.html', views.login, name="login"),
    path('register.html', views.register, name="register"),
    path('somos.html', views.somos, name="somos"),
    
    path('agregar/', views.agregar_receta, name="agregar_receta"),
    path('listar/', views.listar_receta, name="listar_receta"),
    path('modificar/<id>/', views.modificar_receta, name="modificar_receta"),
    path('eliminar/<id>/', views.eliminar_receta , name="eliminar_receta"),

    path('pedidos.html', views.ListarProductos.as_view(), name="pedido"),
    path('agrega_prod.html', views.ProductoCreateView.as_view(), name="agregar"),
    path('modificar_prod.html/<pk>/', views.ProductoUpdateView.as_view(), name="modificar"),

]
