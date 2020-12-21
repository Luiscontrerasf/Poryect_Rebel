from django.contrib import admin
from . models import producto
#rom ckeditor.fields import RichTextField
# Register your models here.
admin.site.register(producto)
#Agrega campos adicionales
#class ProductoAdmin(admin.ModelAdmin):
 #   list_display = (
  #      'tipo_prod',
   #     'descripcion',
    #    'price',
    #)

#admin.site.register(producto,ProductoAdmin)    