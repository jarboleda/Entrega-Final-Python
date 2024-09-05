from django.urls import path
from Usuarios import views
from django.contrib.auth.views import LogoutView
from .views import custom_logout

urlpatterns = [
    path('login/', views.login_request, name='Login'),
    path('register/', views.register, name='Register'),
    path('logout/', custom_logout, name="Logout"),    
    path('edit/', views.edit, name='Edit'),
    path('cambiarPass/', views.cambiarPass.as_view(), name='cambiarPass'),    

]

