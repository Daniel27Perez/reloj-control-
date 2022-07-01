from datetime import datetime
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Horario(models.Model):
    nombreHorario = models.CharField(verbose_name='Horario', max_length=100)
    lunesE = models.TimeField( ("Lunes Entrada") )
    lunesS = models.TimeField( ("Lunes Salida") )
    martesE = models.TimeField( ("Martes Entrada") )
    martesS = models.TimeField( ("Martes Salida") )
    miercolesE = models.TimeField( ("Miercoles Entrada") )
    miercolesS = models.TimeField( ("Miercoles Salida") )
    juevesE = models.TimeField( ("Jueves Entrada") )
    juevesS = models.TimeField( ("Jueves Salida") )
    viernesE = models.TimeField( ("Viernes Entrada") )
    viernesS = models.TimeField( ("Viernes Salida") )
    

def __str__(self):
    return self.nombreHorario

class Control(models.Model):
    titulo = models.CharField(max_length=500, default='Entrada', editable=False)
    usuario = models.ForeignKey(User, default=User , on_delete=models.DO_NOTHING, verbose_name='Usuario')
    fecha = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.titulo
