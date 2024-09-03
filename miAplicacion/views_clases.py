from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Grupos, Supervisores, Usuarios

class gruposClist(LoginRequiredMixin, ListView):
    model = Grupos
    template_name = 'miAplicacion/vistasClases/grupos.html'


class supervisoresClist(LoginRequiredMixin, ListView):
    model = Supervisores
    template_name = 'miAplicacion/vistasClases/supervisores.html'


class usuariosClist(ListView):
    model = Usuarios
    template_name = 'miAplicacion/vistasClases/usuarios.html'


class gruposCborrar(DeleteView):
    model = Grupos
    success_url = reverse_lazy('gruposClist')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)

class supervisoresCborrar(DeleteView):
    model = Supervisores
    success_url = reverse_lazy('supervisoresClist')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)
    
class usuariosCborrar(DeleteView):
    model = Usuarios
    success_url = reverse_lazy('usuariosClist')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)
    

def inicioSesion(req):
    pass

