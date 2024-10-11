from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Registro(AbstractBaseUser):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    password = models.CharField(max_length=128)  # Almacenaremos la contraseña cifrada
    last_login = models.DateTimeField(default=timezone.now)  # Campo para el último inicio de sesión

    def set_password(self, raw_password):
        """Cifra la contraseña usando el sistema de hashing de Django."""
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        """Verifica la contraseña."""
        return check_password(raw_password, self.password)

    def update_last_login(self):
        """Actualiza el campo last_login al iniciar sesión."""
        self.last_login = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.nombre}-{self.apellido}"


