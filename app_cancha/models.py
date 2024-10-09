from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Registro(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=50)
    password = models.CharField(max_length=150)



    def __str__(self):
        return f"{self.nombre} - {self.apellido}"


    
