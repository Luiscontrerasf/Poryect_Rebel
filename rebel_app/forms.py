from django import forms
from django.forms import fields
from .models import Receta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RecetaForm(forms.ModelForm):
    
    class Meta:
        model = Receta
        fields = '__all__'

class CustomUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1','password2']