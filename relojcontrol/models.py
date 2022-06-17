from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Entrada(models.model):
    titulo = models.CharField(verbose_name= 'Titulo', MAX_LENGTH = 100)
