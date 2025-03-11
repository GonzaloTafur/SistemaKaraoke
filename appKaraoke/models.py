from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=80)
    dni = models.CharField(max_length=8)
    numero = models.CharField(max_length=9, blank=True)
    estado = models.BooleanField(default=True)

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

class Categoria(models.Model):
    nombre = models.CharField(max_length=20)
    estado = models.BooleanField(default=True)

class Producto(models.Model):
    nombre = models.CharField(max_length=70)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.FloatField()
    foto = models.ImageField(upload_to="producto/", null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

class Orden(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    #producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto)
    total = models.FloatField()
    hora = models.TimeField()
    estado = models.BooleanField(default=True)