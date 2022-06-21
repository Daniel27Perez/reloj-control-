from django.shortcuts import render

# Create your views here.

def ingreso(request):
    return render(request, 'relojcontrol/ingreso.html', {})
