from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('Tortas.html', views.torta, name="torta"),
    path('Dulces.html', views.dulce, name="dulce"),
    path('Salados.html', views.salado, name="salado"),
    path('contacto.html', views.contacto, name="contacto"),
    path('login.html', views.login, name="login"),
    path('register.html', views.register, name="register"),
    path('somos.html', views.somos, name="somos"),
]