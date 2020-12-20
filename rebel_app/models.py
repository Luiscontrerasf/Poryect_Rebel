from django.db import models

# Create your models here.


class producto(models.Model):
    name = models.CharField(max_length=30)
    tipo_prod = models.CharField('Tipo',max_length=10)#,choices=tipo_prod_CHOISES)    
    description = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    imagen = models.ImageField()

    def __str__(self):
        return self.name


class usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido  = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre + ' ' + self.apellido + ' ' + self.email + ' ' + self.telefono