from django.db import models
#from applications.servicio.models import models
# Create your models here.
class producto(models.Model):
    
    #tipo_prod_CHOISES = (
     #   ('0','DULCE'),
      #  ('1','SALADO'),
       # ('2','OTROS')
    #)

    name = models.CharField(max_length=30)
    tipo_prod = models.CharField('Tipo',max_length=10)#,choices=tipo_prod_CHOISES)    
    description = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    imagen = models.ImageField()
    #servicio = models.ForeignKey(servicio, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name  
    

