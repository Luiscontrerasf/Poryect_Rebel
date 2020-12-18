from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('listar-todo-prod/', views.listaAllProducts.as_view()),
]
