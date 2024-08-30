from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your views here.
class nuevoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    idioma = forms.CharField(max_length=50)

class buscar(forms.Form):
    tipo = forms.CharField(max_length=1)
    codigo = forms.IntegerField(
        validators=[
            MinValueValidator(10000),
            MaxValueValidator(99999)
        ]        
    )