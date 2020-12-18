from django.shortcuts import render
from django.views.generic import  TemplateView, ListView

# Create your views here.
class index(TemplateView):
    template_name='home/index.html'


    