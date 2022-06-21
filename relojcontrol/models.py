from datetime import datetime
from pickle import FALSE, TRUE
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Entrada(models.Model):
    titulo = models.DateTimeField(("Ingreso"), default=datetime.now, editable=False)
