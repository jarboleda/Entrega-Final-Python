from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .models import Grupos, Supervisores, Usuarios

class gruposClist(ListView):
    model = Grupos
    template_name = 'miAplicacion/vistasClases/grupos.html'


class supervisoresClist(ListView):
    model = Supervisores
    template_name = 'miAplicacion/vistasClases/supervisores.html'


class usuariosClist(ListView):
    model = Usuarios
    template_name = 'miAplicacion/vistasClases/usuarios.html'


class gruposCborrar(DeleteView):
    model = Grupos
    success_url = reverse_lazy('gruposClist')
    template_name = 'miAplicacion/vistasClases/grupos.html'


def inicioSesion(req):
    pass

