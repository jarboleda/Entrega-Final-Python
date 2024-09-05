from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegisterForm, UserForm
from Usuarios.models import Imagen
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from datetime import datetime

def custom_logout(request):

    logout(request)
    return redirect('inicio')


def login_request(request):

    hoy = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')

    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return redirect('inicio')
                # return render(request, "miAplicacion/index.html")

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "Usuarios/login.html", {"form": form, "msg_login": msg_login, 'dia_hora': hoy})


def register(request):

    hoy = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')

    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Si los datos ingresados en el form son válidos, con form.save()
            # creamos un nuevo user usando esos datos
            form.save()
            return redirect('inicio')
        
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(request,"Usuarios/registro.html" ,  {"form":form, "msg_register": msg_register, 'dia_hora': hoy})


@login_required
def edit(request):

    hoy = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')

    usuario = request.user
    
    if request.method == 'POST':
        # Se crea un formulario utilizando la instancia del usuario actual
        form = UserForm(request.POST, request.FILES, instance=usuario)

        if form.is_valid():
            if form.cleaned_data.get('imagen'):
                if Imagen.objects.filter(user = usuario).exists():
                    usuario.imagen.imagen = form.cleaned_data.get('imagen')
                    usuario.imagen.save()

                else:
                    avatar = Imagen(user=usuario, imagen = form.cleaned_data.get('imagen'))
                    avatar.save()

            form.save()
            return redirect(reverse_lazy('inicio'))
    
    else:
        # Si la solicitud es GET, se rellena el formulario con los datos del usuario
        form = UserForm(instance = usuario)
    
    return render(request, 'Usuarios/edit.html', {'form': form, 'usuario': usuario, 'dia_hora': hoy})


class cambiarPass(LoginRequiredMixin, PasswordChangeView):
    # mainaadmin / Password$1
    
    template_name = 'Usuarios/password.html'
    success_url = reverse_lazy('Edit')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoy = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
        context['dia_hora'] = hoy
        return context