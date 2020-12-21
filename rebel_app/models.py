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