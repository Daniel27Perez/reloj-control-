from datetime import datetime
from pickle import FALSE, TRUE
from unittest.util import _MAX_LENGTH
from django.db import models

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
    

def __str__( self ):
    return self.nombreHorario
