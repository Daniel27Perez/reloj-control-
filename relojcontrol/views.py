from django.shortcuts import render
from .models import Entrada

# Create your views here.

def ingreso(request):
    entradas = Entrada.objects.all();
    return render(request, 'relojcontrol/ingreso.html', {'entradas' : entradas})

def home(request):
    return render(request, 'relojcontrol/home.html')



