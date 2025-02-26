from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=80)
    dni = models.CharField(max_length=8)
    numero = models.CharField(max_length=9, blank=True)
    estado = models.BooleanField()

class Mesa(models.Model):
    numero = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    estado = models.BooleanField()
    
class Cancion(models.Model):
    nombre = models.CharField(max_length=50)
    artista = models.CharField(max_length=50)
    modo = models.CharField(max_length=20)
    fecha = models.DateField(auto_now_add=True)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)