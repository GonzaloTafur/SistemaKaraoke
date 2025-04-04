from django.shortcuts import redirect, render
from appKaraoke.models import Cliente, Mesa, MesaCliente, Orden, Producto
from appKaraoke_ordenes.forms import frmMesaCliente, frmOrden

# Create your views here.
def ordenes(request):
    frmorden = frmOrden()
    return render(request, 'ordenes/ordenes.html', {"frmorden":frmorden})

def grabarOrden(request):

    try:
        if request.method == 'POST':
            frmorden = frmOrden(request.POST)

            if frmorden.is_valid():
                cd = frmorden.cleaned_data

                nuevaOrden = frmorden.save(commit=False)
                nuevaOrden.save()
                frmorden.save_m2m()

                print('Se ha guardado todos los datos con exito!')
                return redirect('/ordenes/')
            else:
                return render(request, 'ordenes/ordenes.html', {"frmorden":frmorden})

    except:
        print('No se pudo guardar correctamente'),
        return render(request, 'ordenes/ordenes.html', {"frmorden":frmorden})
    
def listaOrdenes(request):
    lstordenes = Orden.objects.filter(estado=True)
    return render(request, 'ordenes/lista.html', {"lstordenes":lstordenes})

def registrarMesaCliente(request):
    frmmc = frmMesaCliente()
    return render(request, 'ordenes/registrarMesaCliente.html', {"frmmc":frmmc})

def grabarMesaCliente(request):

    if request.method == 'POST':
        frmmc = frmMesaCliente(request.POST)

        if frmmc.is_valid():
            cd = frmmc.cleaned_data

            nuevaMesaCliente = MesaCliente(
                mesa=Mesa.objects.get(id=request.POST['mesa']),
                cliente=Cliente.objects.get(id=request.POST['cliente'])
            )
            nuevaMesaCliente.save()

            print('Se ha guardado todos los datos con exito!')
            return redirect('/ordenes/')
        else:
            print('No se pudo guardar correctamente'),
            return render(request, 'ordenes/ordenes.html', {"frmmc":frmmc})


    return render('/ordenes/')