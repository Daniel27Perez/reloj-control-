from email import message
from pyexpat.errors import messages
from django import views
from django.shortcuts import redirect, render
from .models import Entrada, Horario
from .forms import CustomUserForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .serializers import HorarioSerializers
from rest_framework import viewsets
from django.views.generic import TemplateView

# Create your views here.

def ingreso(request):
    entradas = Entrada.objects.all();
    return render(request, 'relojcontrol/ingreso.html', {'entradas' : entradas})

def home(request):
    return render(request, 'relojcontrol/home.html')
def ejemplo(request):
    return render(request, 'relojcontrol/ejemplo.html')


def registro(request):
    data = {
        'form':CustomUserForm() 
    }
    if request.method == 'POST':
        formulario = CustomUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #redireccionar a pagina principal
            user = authenticate(username= formulario.cleaned_data["username"], password= formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to='home')
        data['form'] = formulario    
    return render(request, 'registration/registro.html', data)

class HorarioView(viewsets.ModelViewSet):
    serializer_class = HorarioSerializers
    queryset = Horario.objects.all();
    

class getCalendar(TemplateView):
    template_name = 'relojcontrol/calendar.html'
    def get_context_data(self, *args, **kwargs):
        pass
        
        



