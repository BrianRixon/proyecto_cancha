from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views




urlpatterns = [

    path('',inicio, name="inicio"),
    path('registro.html', registro, name="registro" ),
    path('registro_exitoso', registro_exitoso, name="registro_exitoso"),
    path('home.html', home, name="home"),
    path('login.html', iniciar_sesion, name="login"),
    path('logout.html', cerrar_session, name = "logout"),
    path('futbol5.html', futbol5, name = "futbol5"),
    path('paddle.html', paddle, name = "paddle"),
    path('tenis.html', tenis, name = "tenis"),
    path("contacto.html", contacto, name="contacto"),
    path("turnos.html", crear_reserva, name="turnos"),
    path("reserva_exitosa.html", reserva_exitosa, name="reserva_exitosa"),
]