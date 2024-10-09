from django.shortcuts import render
from .forms import formRegistro
from .models import *
from django.contrib.auth.hashers import make_password
# Create your views here.

def registro(request):
    if request.method == 'POST':
        nuevo_formulario = formRegistro(request.POST)

        if nuevo_formulario.is_valid():
            data = nuevo_formulario.cleaned_data

            # Verificar que las contraseñas coincidan
            if data['password1'] != data['password2']:
                nuevo_formulario.add_error('password2', 'Las contraseñas no coinciden.')
            else:
                # Crear una nueva instancia del modelo Registro
                nuevo_usuario = Registro(
                    nombre=data['nombre'],
                    apellido=data['apellido'],
                    email=data['email'],
                    telefono=data['telefono'],
                    password=make_password(data['password1'])  # Hash de la contraseña
                )
                nuevo_usuario.save()

                # Redirigir a una página de éxito
                return render(request, 'registro_exitoso.html', {"mensaje": "Registro exitoso"})

    else:
        nuevo_formulario = formRegistro()  # Crear un formulario vacío para GET

    return render(request, 'registro.html', {'nuevo_formulario': nuevo_formulario})




# render de templates
def inicio(request):
    return render(request, "home.html", {})

def registro_exitoso(request):
    return render(request, "registro_exitoso.html", {})

def home(request):
    return render(request, "home.html", {})


