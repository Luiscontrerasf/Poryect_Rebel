from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('Tortas.html', views.torta, name="torta"),
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
]