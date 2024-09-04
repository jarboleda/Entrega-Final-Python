from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from miAplicacion.models import Grupos, Supervisores, Usuarios

# Create your views here.

class buscar(forms.Form):
    tipo = forms.CharField(max_length=1)
    codigo = forms.IntegerField(
        validators=[
            MinValueValidator(10000),
            MaxValueValidator(99999)
        ]        
    )


class gruposEdit(forms.ModelForm):

    ESTADO_CHOICES = [
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    ]

    estado = forms.ChoiceField(choices=ESTADO_CHOICES) 

    class Meta:
        model = Grupos
        fields = ['codigo','creacion','nombre','idioma','estado']

    def __init__(self, *args, **kwargs):
        super(gruposEdit, self).__init__(*args, **kwargs)
        self.fields['codigo'].disabled = True
        self.fields['creacion'].disabled = True


class supervisoresEdit(forms.ModelForm):

    ESTADO_CHOICES = [
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    ]

    estado = forms.ChoiceField(choices=ESTADO_CHOICES)

    class Meta:
        model = Supervisores
        fields = ['codigo','creacion','nombres','idioma','email','estado']

    def __init__(self, *args, **kwargs):
        super(supervisoresEdit, self).__init__(*args, **kwargs)
        self.fields['codigo'].disabled = True
        self.fields['creacion'].disabled = True


class usuariosEdit(forms.ModelForm):

    ESTADO_CHOICES = [
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    ]

    estado = forms.ChoiceField(choices=ESTADO_CHOICES)

    class Meta:
        model = Usuarios
        fields = ['codigo','creacion','nombres','idioma','estado']

    def __init__(self, *args, **kwargs):
        super(usuariosEdit, self).__init__(*args, **kwargs)
        self.fields['codigo'].disabled = True
        self.fields['creacion'].disabled = True

