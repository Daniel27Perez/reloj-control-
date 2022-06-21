from datetime import datetime
from pickle import FALSE, TRUE
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Entrada(models.Model):
    titulo = models.CharField(verbose_name='', max_length=8, default='Ingreso', editable=False)
    entrada = models.DateTimeField(("Ingreso"), default=datetime.now, editable=False)

def __str__(self):
    return self.titulo
