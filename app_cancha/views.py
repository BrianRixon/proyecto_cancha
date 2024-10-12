from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
# Create your views here.

def registro(request):
    if request.method == 'POST':
        nuevo_formulario = formRegistro(request.POST)

        if nuevo_formulario.is_valid():
            data = nuevo_formulario.cleaned_data

            if data['password1'] != data['password2']:
                nuevo_formulario.add_error('password2', 'Las contraseñas no coinciden.')
            else:
                
                nuevo_usuario = Registro(
                    nombre=data['nombre'],
                    apellido=data['apellido'],
                    email=data['email'],
                    telefono=data['telefono'],
                    password=make_password(data['password1'])  # Hash de la contraseña
                )
                nuevo_usuario.save()

                return render(request, 'registro_exitoso.html', {"mensaje": "Registro exitoso"})

    else:
        nuevo_formulario = formRegistro()  

    return render(request, 'registro.html', {'nuevo_formulario': nuevo_formulario})



def iniciar_sesion(request):
    if request.method == 'POST':
        
        formulario = formLogin(request.POST)
        
        if formulario.is_valid():
            
            email = formulario.cleaned_data.get('email')
            password = formulario.cleaned_data.get('password')
            
            try:
               
                usuario = Registro.objects.get(email=email)  
                
               
                if usuario.check_password(password):
                    
                    login(request, usuario)
                    messages.success(request, f"Bienvenido, {usuario.nombre}!")  
                    return render(request,'home.html')  
                else:
                    messages.error(request, "Contraseña incorrecta.")  
            except Registro.DoesNotExist:
                messages.error(request, "Usuario no encontrado.")  
                return render(request, 'login.html', {'formulario': formulario})

    else:
        
        formulario = formLogin()
    
    
    return render(request, 'login.html', {'formulario': formulario})

        

def cerrar_session(request):
    logout(request)
    return render(request, "logout.html", {})


def contacto(request):

    if request.method == 'POST':

        formcontacto = formContacto(request.POST)

        if formcontacto.is_valid():
            nombre = formcontacto.cleaned_data['nombre']
            email = formcontacto.cleaned_data['email']
            mensaje = formcontacto.cleaned_data['mensaje']

            mensaje_completo = f"De: {nombre} <{email}>\n\nMensaje\n{mensaje}"

            send_mail(f'Consulta de {nombre} desde el sitio web',  # Asunto
                mensaje_completo,  
                email,  
                ['brianrixon_mdp@hotmail.com'],  
                fail_silently=False,
            )

        messages.success(request, "Tu consulta fue enviada!")
        return render(request, "home.html", {})
    
    else:

        formcontacto = formContacto()

        return render(request,"contacto.html",{'formcontacto':formcontacto})


#@login_required
def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False) 
            reserva.usuario = request.user 
            reserva.estado = 'pendiente'  
            reserva.save()  
            return render(request,'reserva_exitosa.html',{})
    else:
        form = ReservaForm()
    
    return render(request, 'turnos.html', {'form': form})









# render de templates


def inicio(request):
    return render(request, "home.html", {})

def registro_exitoso(request):
    return render(request, "registro_exitoso.html", {})

def home(request):
    return render(request, "home.html", {})


def paddle(request):
    return render(request, "paddle.html", {})

def futbol5(request):
    return render(request, "futbol5.html", {})

def tenis(request):
    return render(request, "tenis.html", {})

def reserva_exitosa(request):
    return render(request,"reserva_exitosa.html",{})





