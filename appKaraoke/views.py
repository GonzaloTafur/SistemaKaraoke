from django import forms
from django.shortcuts import redirect, render
from appKaraoke.forms import frmOrdenCancion
from appKaraoke.models import Cancion, Mesa, MesaCliente, OrdenCancion

# Create your views here.

# INICIO DE SESION
def login(request):
    return render(request, "login.html")

# USUARIO DJ
def dj(request):
    #cbxcanciones = Cancion.objects.all()
    #cbxmesas = MesaCliente.objects.all()
    lstoc = OrdenCancion.objects.filter(estado=True)
    frmoc = frmOrdenCancion(request.POST)
    return render(request, "dj/canciones.html", {"frmoc":frmoc, "lstoc":lstoc})

def grabar_cancion(request):

    if request.method=="POST":
        frmoc = frmOrdenCancion(request.POST)

        if frmoc.is_valid():
            cd = frmoc.cleaned_data
            
            nuevaCancion = OrdenCancion(
                cancion = Cancion.objects.get(id = request.POST['cancion']),
                mesa_cliente = MesaCliente.objects.get(id = request.POST['mesa_cliente'])
            )
            nuevaCancion.save()

            print("Se registró correctamente")
            return redirect("/dj/")
        
    else:
        print("No se pudo guardar")
        return redirect("/dj/")

def eliminarOrdenCancion(request, id):
    
    oc = OrdenCancion.objects.get(id=id)

    if oc.estado == True:
        oc.estado = False
        oc.save()
        
    return redirect("/dj/")