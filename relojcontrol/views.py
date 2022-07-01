from datetime import datetime
from django.core.mail import send_mail
from pyexpat.errors import messages
from django.conf import settings
from django.shortcuts import redirect, render
from .models import Horario
from .forms import CustomUserForm, FormularioEntrada, FormularioSalida
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .serializers import HorarioSerializers
from rest_framework import viewsets



# Create your views here.


def home(request):
    return render(request, 'relojcontrol/home.html')
def Feriados(request):
    return render(request, 'relojcontrol/feriados.html')


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
    
def Reporte(request):
    if request.method == "POST":
        subject = request.POST["asunto"]
        message = request.POST["mensaje"] + " " + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["danielignacio2178@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)
        messages.success(request, "Reporte enviado correctamente")
        return redirect(to='home')
    return render(request, "relojcontrol/reporte.html" )
        
def Calendario(request):
    return render(request, 'relojcontrol/calendar.html')

def Asistencia(request):
    return render(request, 'relojcontrol/asistencia.html')


def ingreso(request):
    if request.method == 'POST':
        form = FormularioEntrada(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "ingreso exitoso")
            return redirect(to='home')
    else:
        form = FormularioEntrada()  
             
    return render(request, 'relojcontrol/ingreso.html', {'form':form })

def Termino(request):
    if request.method == 'POST':
        formu = FormularioSalida(request.POST)
        if formu.is_valid():
            formu.save()
            messages.success(request, "Salida exitoso")
            return redirect(to='home')
    else:
        formu = FormularioSalida()  
             
    return render(request, 'relojcontrol/salida.html', {'formu':formu })