from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Grupos, Supervisores, Usuarios
from .forms import gruposEdit, supervisoresEdit, usuariosEdit


class gruposClist(LoginRequiredMixin, ListView):
    model = Grupos
    template_name = 'miAplicacion/vistasClases/grupos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoy = timezone.now().strftime('%d/%m/%Y, %H:%M:%S')
        context['dia_hora'] = hoy
        return context


class supervisoresClist(LoginRequiredMixin, ListView):
    model = Supervisores
    template_name = 'miAplicacion/vistasClases/supervisores.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoy = timezone.now().strftime('%d/%m/%Y, %H:%M:%S')
        context['dia_hora'] = hoy
        return context


class usuariosClist(ListView):
    model = Usuarios
    template_name = 'miAplicacion/vistasClases/usuarios.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoy = timezone.now().strftime('%d/%m/%Y, %H:%M:%S')
        context['dia_hora'] = hoy
        return context


class gruposEditar(LoginRequiredMixin, UpdateView):
    model = Grupos
    form_class = gruposEdit
    template_name = 'miAplicacion/vistasClases/gruposEditar.html'
    success_url = reverse_lazy('gruposClist')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoy = timezone.now().strftime('%d/%m/%Y, %H:%M:%S')
        context['dia_hora'] = hoy
        return context


class supervisoresEditar(LoginRequiredMixin, UpdateView):
    model = Supervisores
    form_class = supervisoresEdit
    template_name = 'miAplicacion/vistasClases/gruposEditar.html'
    success_url = reverse_lazy('supervisoresClist')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoy = timezone.now().strftime('%d/%m/%Y, %H:%M:%S')
        context['dia_hora'] = hoy
        return context
    

class usuariosEditar(LoginRequiredMixin, UpdateView):
    model = Usuarios
    form_class = usuariosEdit
    template_name = 'miAplicacion/vistasClases/gruposEditar.html'
    success_url = reverse_lazy('usuariosClist')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoy = timezone.now().strftime('%d/%m/%Y, %H:%M:%S')
        context['dia_hora'] = hoy
        return context
    

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
    

