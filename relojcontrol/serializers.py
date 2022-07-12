from rest_framework import serializers
from .models import Horario, Control, ControlSalida

class HorarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Horario  
        fields = ['id', 'nombreHorario', 'lunesE', 'lunesS' ,'martesE', 'martesS','miercolesE', 
                  'miercolesS', 'juevesE', 'juevesS' ,'viernesE', 'viernesS']

class ControlSerializers(serializers.ModelSerializer):
    class Meta:
        model = Control  
        fields = ['id', 'titulo', 'usuario', 'fecha']

class ControlSalidaSerializers(serializers.ModelSerializer):
    class Meta:
        model = ControlSalida  
        fields = ['id', 'titulo', 'usuario', 'fecha']