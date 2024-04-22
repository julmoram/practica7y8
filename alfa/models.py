from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Floreria(models.Model):
    nombre= models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
    cantidad = models.CharField(max_length=50)
    paquete = models.CharField(max_length=50, choices=[('1', 'paquete A'), ('2', 'paquete B'), ('3', 'paquete C')])
    fecha_creado= models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombre}-{self.color}-{self.fecha_creado}"
    
class Follaje(models.Model):
    nombre= models.CharField(max_length=50)
    color= models.CharField(max_length=50)
    models.CharField(max_length=50, choices=[('1', 'paquete A'), ('2', 'paquete B'), ('3', 'paquete C')])
    
def __str__(self):
        return f"{self.nombre}-{self.color}-{self.fecha_creado}"