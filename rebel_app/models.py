from django.db import models
from django.core.files.storage import FileSystemStorage
from django.utils import timezone

# Create your models here.


fs = FileSystemStorage(location='/media/photos')

class Receta(models.Model):
    nombre = models.CharField(max_length=30)
    ingredientes = models.TextField();
    preparacion = models.TextField();
    fecha = models.DateTimeField(default=timezone.now);
    imagen = models.ImageField(upload_to="recetas", null = True)
    
    def __str__(self):
        return self.nombre
class producto(models.Model):
    name = models.CharField(max_length=30)
    tipo_prod = models.CharField('Tipo',max_length=10)#,choices=tipo_prod_CHOISES)    
    description = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    imagen = models.ImageField()

    def __str__(self):
        return self.name + ' ' + self.tipo_prod + ' ' + self.description + ' ' + self.price 

class usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido  = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre + ' ' + self.apellido + ' ' + self.email + ' ' + self.telefono
