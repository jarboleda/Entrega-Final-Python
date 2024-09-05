from django.urls import path
from . import views
from .views_clases import *

urlpatterns = [
    path('', views.Inicio, name='inicio'),
    path('gruposForm/', views.gruposForm, name='gruposForm'),
    path('supervisoresForm/', views.supervisoresForm, name='supervisoresForm'),
    path('usuariosForm/', views.usuariosForm, name='usuariosForm'),
    path('buscar/', views.buscar, name='buscar'),
    path('about/', views.about, name='about'),

]

urls_vistas_clases = [
    path('gruposClist/', gruposClist.as_view(), name='gruposClist'),
    path('gruposCborrar/<int:pk>/', gruposCborrar.as_view(), name='gruposCborrar'),
    path('editarGrupos/<int:pk>/', gruposEditar.as_view(), name='editarGrupos'),

    path('supervisoresClist/', supervisoresClist.as_view(), name='supervisoresClist'),
    path('supervisoresCborrar/<int:pk>/', supervisoresCborrar.as_view(), name='supervisoresCborrar'),
    path('editarSupervisores/<int:pk>/', supervisoresEditar.as_view(), name='editarSupervisores'),

    path('usuariosClist/', usuariosClist.as_view(), name='usuariosClist'),
    path('usuariosCborrar/<int:pk>/', usuariosCborrar.as_view(), name='usuariosCborrar'),
    path('editarUsuarios/<int:pk>/', usuariosEditar.as_view(), name='editarUsuarios'),

]

urlpatterns += urls_vistas_clases