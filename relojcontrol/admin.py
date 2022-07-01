from django.contrib import admin
from .models import Horario, Control, ControlSalida
# Register your models here.

admin.site.register(Horario)
admin.site.register(Control)
admin.site.register(ControlSalida)