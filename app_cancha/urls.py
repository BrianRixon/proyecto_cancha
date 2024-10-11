from django.urls import path
from .views import *




urlpatterns = [

    path('',inicio, name="inicio"),
    path('registro.html', registro, name="registro" ),
    path('registro_exitoso', registro_exitoso, name="registro_exitoso"),
    path('home.html', home, name="home"),
    path('login.html', iniciar_sesion, name="login"),
    path('logout.html',cerrar_session,name="logout")

]
