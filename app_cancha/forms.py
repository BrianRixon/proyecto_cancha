from django import forms

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
