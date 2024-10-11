from django.shortcuts import render
from .forms import formRegistro, formLogin
from .models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import check_password
from django.contrib import messages
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



def iniciar_sesion(request):
    if request.method == 'POST':
        # Crear una instancia del formulario con los datos del POST
        formulario = formLogin(request.POST)
        
        if formulario.is_valid():
            # Extraer los datos del formulario
            email = formulario.cleaned_data.get('email')
            password = formulario.cleaned_data.get('password')
            
            try:
                # Obtener el usuario con ese email
                usuario = Registro.objects.get(email=email)  
                
                # Verificar si la contraseña es correcta
                if usuario.check_password(password):
                    # Si la autenticación es exitosa, iniciar sesión
                    login(request, usuario)
                    messages.success(request, f"Bienvenido, {usuario.nombre}!")  # Mensaje de éxito
                    return render(request,'home.html')  # Redirigir a la página de inicio u otra página
                else:
                    messages.error(request, "Contraseña incorrecta.")  # Mensaje de error
            except Registro.DoesNotExist:
                messages.error(request, "Usuario no encontrado.")  # Mensaje de error
                return render(request, 'login.html', {'formulario': formulario})

    else:
        # Si el método es GET, renderizar el formulario vacío
        formulario = formLogin()
    
    # Renderizar el formulario de inicio de sesión con mensajes de error (si los hay)
    return render(request, 'login.html', {'formulario': formulario})

        


def cerrar_session(req):
    pass














# render de templates


def inicio(request):
    return render(request, "home.html", {})

def registro_exitoso(request):
    return render(request, "registro_exitoso.html", {})

def home(request):
    return render(request, "home.html", {})


