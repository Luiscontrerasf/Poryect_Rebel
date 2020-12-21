from django.db import models
from applications.producto.models import producto
# Create your models here.

class servicio(models.Model):
    banqueteria = models.CharField(max_length=50)
    pack = models.CharField('Promos',max_length=50)
    precio = models.CharField(max_length=50)
    stock = models.BooleanField(default=False)    
    producto = models.ManyToManyField(producto)

    def __str__(self):
        return self.banqueteria + ' ' + self.pack + ' ' + self.precio
    
