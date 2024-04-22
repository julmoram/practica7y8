from django.forms import ModelForm  
from .models import Floreria  

class ComprarForm(ModelForm):
    class Meta:
        model = Floreria  
        fields = ['nombre', 'color', 'cantidad', 'paquete', 'usuario']