from django.shortcuts import redirect, render
from .models import Entrada
from .forms import CustomUserForm
from django.contrib.auth import login, authenticate

# Create your views here.

def ingreso(request):
    entradas = Entrada.objects.all();
    return render(request, 'relojcontrol/ingreso.html', {'entradas' : entradas})

def home(request):
    return render(request, 'relojcontrol/home.html')

def registro(request):
    data = {
        'form':CustomUserForm() 
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #redireccionar a pagina principal
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to = 'home')
            
    return render(request, 'registration/registro.html', data)



