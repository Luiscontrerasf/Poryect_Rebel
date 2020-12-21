from django import forms
from django.forms import fields
from .models import Receta

class RecetaForm(forms.ModelForm):
    
    class Meta:
        model = Receta
        fields = '__all__'