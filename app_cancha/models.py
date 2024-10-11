from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth import get_user_model

class Registro(AbstractBaseUser):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    password = models.CharField(max_length=128)  
    last_login = models.DateTimeField(default=timezone.now)  

    def set_password(self, raw_password):
        
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        
        return check_password(raw_password, self.password)

    def update_last_login(self):

        self.last_login = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.nombre}-{self.apellido}"




class TipoCancha(models.Model):
    TIPO_DE_CANCHA = [
        ('tenis1', 'tenis1'),
        ('tenis2', 'tenis2'),
        ('paddle1','paddle1'),
        ('paddle2','paddle2'),
        ('paddle3','paddle3'),
        ('futbol','futbol'),
    ]
    tipo = models.CharField(max_length=25,choices=TIPO_DE_CANCHA, unique=True)
    descripcion = models.TextField(blank=True, null=True) 

    def __str__(self):
        return f"{self.tipo}"
    

class Reserva(models.Model):
        usuario = models.ForeignKey(Registro, on_delete=models.CASCADE)  # Relación con el modelo Registro
        cancha = models.ForeignKey(TipoCancha, on_delete=models.CASCADE)  # Relación con el modelo TipoCancha
        fecha_reserva = models.DateTimeField(default=timezone.now)
        duracion = models.PositiveIntegerField(help_text="Duración en minutos")
        estado = models.CharField(max_length=10, default='pendiente')  

        def __str__(self):
            return f"Reserva {self.id} - {self.usuario.nombre} {self.usuario.apellido} - {self.cancha.tipo}"

        class Meta:
            ordering = ['fecha_reserva'] 