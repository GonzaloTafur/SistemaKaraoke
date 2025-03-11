from django import forms
from django.shortcuts import redirect, render
from appKaraoke.models import Cancion, Mesa

# Create your views here.

# INICIO DE SESION
def login(request):
    return render(request, "login.html")

# USUARIO DJ
def dj(request):
    lstcanciones = Cancion.objects.all()
    lstmesas = Mesa.objects.all()

    return render(request, 
                    "dj/canciones.html", 
                    {"lstcanciones":lstcanciones, 
                     "lstmesas":lstmesas})

def grabar_cancion(request):
        
        #Mesa.objects.get(request.POST["mesa"])
        '''
        nombre = request.POST["nombre"]
        artista = request.POST["artista"]
        modo = request.POST["modo"]
        #mesa = request.POST["mesa"]
        mesa = Mesa.objects.get(id = request.POST['mesa'])
        '''

        nuevaCancion = Cancion.objects.create(
            nombre = request.POST["nombre"],
            artista= request.POST["artista"],
            modo = request.POST["modo"],
            mesa = Mesa.objects.get(id = request.POST['mesa'])
        )

        #print("Se registró correctamente")
        return redirect("/dj/")
