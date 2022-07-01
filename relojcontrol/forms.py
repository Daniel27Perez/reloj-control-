from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User                                       
from relojcontrol.models import Control
class CustomUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2' ]

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class FormularioEntrada(forms.ModelForm):
    class Meta:
        model=Control
        fields=('usuario', 'fecha', )
        
widgets = {
            
            'fecha': DateTimeInput(attrs={'class': 'form-control'}),
            
        }
