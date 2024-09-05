from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from datetime import date, datetime
from miAplicacion.models import Grupos, Supervisores, Usuarios
from django.contrib.auth.decorators import login_required

# Create your views here.

def Inicio(request):
# Vista de inicio

    hoy = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
    return render(request, "miaplicacion/index.html", {'dia_hora': hoy})

def about(request):

    hoy = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
    return render(request, 'miaplicacion/about.html', {'dia_hora': hoy})

@login_required
def gruposForm(req):
# Vista del formulario para agregar nuevos grupos

    hoy = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')

    if req.method == 'POST':
        cod = str(random.randint(10000,99999))
        sta = "A"
        cre = date.today()
        grupo = Grupos(codigo=cod, nombre=req.POST['nombre'], idioma=req.POST['idioma'], estado=sta, creacion=cre)
        grupo.save()

        return redirect('gruposClist')

    return render(req, 'miaplicacion/gruposForm.html', {'dia_hora': hoy})


@login_required
def supervisoresForm(req):
# Vista del formulario para agregar nuevos supervisores

    hoy = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')

    if req.method == 'POST':
        cod = str(random.randint(10000,99999))
        sta = "A"
        cre = date.today()
        grupo = Supervisores(codigo=cod, nombres=req.POST['nombre'], idioma=req.POST['idioma'], email=req.POST['email'], estado=sta, creacion=cre)
        grupo.save()

        return redirect('supervisoresClist')
    
    return render(req, 'miaplicacion/supervisoresForm.html', {'dia_hora': hoy})


@login_required
def usuariosForm(req):
# Vista del formulario para agregar nuevos usuarios

    hoy = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')

    if req.method == 'POST':
        cod = str(random.randint(10000,99999))
        sta = "A"
        cre = date.today()
        grupo = Usuarios(codigo=cod, nombres=req.POST['nombre'], idioma=req.POST['idioma'], estado=sta, creacion=cre)
        grupo.save()

        return redirect('usuariosClist')
    
    return render(req, 'miaplicacion/usuariosForm.html', {'dia_hora': hoy})


def buscar(req):
# Vista del formulario para buscar
    
    if req.GET['codigo']:
        cod = req.GET['codigo']
        tipo = req.GET['tipo']

        if tipo == '1':
            obj = Grupos
        elif tipo == '2':
            obj = Supervisores
        else:
            obj = Usuarios

        datos = obj.objects.filter(codigo__icontains=cod)

        hoy = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
        return render(req, 'miaplicacion/resultados.html', {'datos': datos, 'codigo': cod, 'tipo': tipo, 'dia_hora': hoy})
  
    else:
        # return render(req, 'miaplicacion/index.html')
        return redirect('inicio')

