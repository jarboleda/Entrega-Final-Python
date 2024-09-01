from django.urls import path
from . import views


urlpatterns = [
    path('', views.Inicio, name='inicio'),
    path('gruposList/', views.gruposList, name='gruposList'),
    path('gruposForm/', views.gruposForm, name='gruposForm'),
    path('gruposBorrar/<codigoBorrar>/', views.gruposBorrar, name='gruposBorrar'),

    path('supervisoresList/', views.supervisoresList, name='supervisoresList'),
    path('supervisoresForm/', views.supervisoresForm, name='supervisoresForm'),
    path('supervisoresBorrar/<codigoBorrar>/', views.supervisoresBorrar, name='supervisoresBorrar'),

    path('usuariosList/', views.usuariosList, name='usuariosList'),
    path('usuariosForm/', views.usuariosForm, name='usuariosForm'),
    path('usuariosBorrar/<codigoBorrar>/', views.usuariosBorrar, name='usuariosBorrar'),

    path('buscar/', views.buscar, name='buscar'),
    path('nuevoFormulario/', views.nuevoForm, name='nuevoFormulario'),

]