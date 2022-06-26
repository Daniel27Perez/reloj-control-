from rest_framework import serializers
from .models import Horario

class HorarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Horario  
        fields = ['id', 'nombreHorario', 'lunesE', 'lunesS' ,'martesE', 'martesS','miercolesE', 
                  'miercolesS', 'juevesE', 'juevesS' ,'viernesE', 'viernesS']