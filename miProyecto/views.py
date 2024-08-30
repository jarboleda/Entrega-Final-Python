from django.http import HttpResponse
from datetime import date, datetime
from django.template import Template, Context
from django.template import loader

from miAplicacion.models import Grupos, Supervisores, Usuarios
import random

def agregaGrupo(req, nom, idi):

    cod = str(random.randint(10000,99999))
    sta = "A"
    grupo = Grupos(codigo=cod, nombre=nom, idioma=idi, estado=sta, creacion=date.today())
    grupo.save()

    return HttpResponse("Se agregó el grupo")
