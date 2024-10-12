from django import forms
from .models import Reserva

class formRegistro(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=50)
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='repetir contraseña', widget=forms.PasswordInput)


class formLogin(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(label='contraseña', widget=forms.PasswordInput) 


class formContacto(forms.Form):

    nombre = forms.CharField(max_length=100, label="Nombre")
    email = forms.EmailField(label="Correo Electrónico")
    mensaje = forms.CharField(widget=forms.Textarea, label="Mensaje")

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['cancha', 'fecha_reserva', 'duracion']
        widgets = {
            'fecha_reserva': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'duracion': forms.NumberInput(attrs={'min': 1}),
        }