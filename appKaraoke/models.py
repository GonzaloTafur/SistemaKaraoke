from django.db import models

# Create your models here.
class Genero(models.Model):
    nombre = models.CharField(max_length=20)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
class Cancion(models.Model):

    nombre = models.CharField(max_length=50)
    artista = models.CharField(max_length=50)
    #genero = models.CharField(max_length=20, null=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, null=True, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre + ' - ' + self.artista

class Mesa(models.Model):
    numero = models.CharField(max_length=50)
    estado = models.BooleanField()

    def __str__(self):
        return self.numero

class Cliente(models.Model):
    nombre = models.CharField(max_length=80)
    dni = models.CharField(max_length=8, blank=True)
    numero = models.CharField(max_length=9, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre + ' - ' + self.dni

class MesaCliente(models.Model):
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.cliente.nombre + ' - Mesa ' + self.mesa.numero

class OrdenCancion(models.Model):
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE, null=True, blank=True)
    mesa_cliente = models.ForeignKey(MesaCliente, on_delete=models.CASCADE, null=True, blank=True)
    estado = models.BooleanField(default=True)

class Categoria(models.Model):
    nombre = models.CharField(max_length=20)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=70)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.FloatField()
    foto = models.ImageField(upload_to="producto/", null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
class Orden(models.Model):
    #mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    #producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    mesa_cliente = models.ForeignKey(MesaCliente, on_delete=models.CASCADE, null=True, blank=True)
    producto = models.ManyToManyField(Producto)
    total = models.FloatField()
    hora = models.TimeField(auto_now_add=True)
    fecha = models.DateField(auto_now_add=True, null=True)
    estado = models.BooleanField(default=True)