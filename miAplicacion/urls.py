from django.urls import path
from . import views
from .views_clases import *

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

]

urls_vistas_clases = [
    path('gruposClist/', gruposClist.as_view(), name='gruposClist'),
    path('gruposCborrar/<int:pk>/', gruposCborrar.as_view(), name='gruposCborrar'),

    path('supervisoresClist/', supervisoresClist.as_view(), name='supervisoresClist'),
    path('supervisoresCborrar/<int:pk>/', supervisoresCborrar.as_view(), name='supervisoresCborrar'),

    path('usuariosClist/', usuariosClist.as_view(), name='usuariosClist'),
    path('usuariosCborrar/<int:pk>/', usuariosCborrar.as_view(), name='usuariosCborrar'),

]

urlpatterns += urls_vistas_clases