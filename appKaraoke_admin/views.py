from django.shortcuts import get_object_or_404, redirect, render

from appKaraoke.models import Cancion, Categoria, Cliente, Genero, Mesa, Orden, Producto
from appKaraoke_admin.forms import frmCancion, frmCategoria, frmCliente, frmGenero, frmMesa, frmProducto

# Create your views here.

def panel_admin(request):
    return render(request, "administracion.html")

# GENEROS
def generos(request):
    lstgeneros = Genero.objects.all()
    frmgen = frmGenero()
    return render(request,"canciones/generos.html", {"lstgeneros":lstgeneros, "frmgen":frmgen})

def grabarGenero(request):
    if request.method == "POST":
        frmcat = frmGenero(request.POST)

        if frmcat.is_valid():
            cd = frmcat.cleaned_data

            nuevoGenero = Genero(
                nombre = request.POST["nombre"]
            )
            nuevoGenero.save()
            print('Se han guardado todos los datos con exito')
            return redirect('/gestion_generos/')
        
        else:
            print('No se ha podido guardar')
            return redirect('/gestion_generos/')

# CANCIONES
def canciones(request):
    lstcanciones = Cancion.objects.all()
    return render(request,"canciones/gestionar.html", {"lstcanciones":lstcanciones})

def registrarCancion(request):
    frmcancion = frmCancion()
    return render(request,"canciones/registrar.html", {"frmcancion":frmcancion})

def grabarCancion(request):
    if request.method == "POST":
        frmcancion = frmCancion(request.POST)
        if frmcancion.is_valid():
            cd = frmcancion.cleaned_data

            nuevaCancion = Cancion(
                nombre=request.POST["nombre"],
                artista=request.POST["artista"],
                #genero=request.POST["genero"]
                genero=Genero.objects.get(id = request.POST["genero"])
            )
            nuevaCancion.save()
            return redirect("/gestion_canciones/")
    else:
        print("No se ha podido guardar")
        return redirect("/registrar_cancion/")

def editar_ca(request, id):
    ca = Cancion.objects.get(id=id)
    return render(request, "canciones/actualizar.html", {'ca':ca})

def actualizar_ca(request):
    ca = get_object_or_404(Cancion, id=request.POST.get('id'))

    if request.method == 'POST':
        ca.nombre=request.POST.get('nombre')
        ca.artista=request.POST.get('artista')
        #ca.genero=request.POST.get('genero')
        #ca.genero=Genero.objects.get(id = request.POST["genero"])
        ca.save()

        return redirect('/gestion_canciones/')

def eliminar_ca(request, id):
    ca = Cancion.objects.get(id=id)
    
    if ca.estado == True:
        ca.estado = False
        ca.save()
    else:
        print('No se pudo eliminar porque ya está desactivado')
        return redirect('/gestion_canciones/')    

    return redirect('/gestion_canciones/')


# MESAS
def mesas(request):
    lstmesas = Mesa.objects.all()
    return render(request,"mesas/gestionar.html", {"lstmesas":lstmesas})

def registrar_m(request):
    #lstclientes = Cliente.objects.all()
    frmmesa = frmMesa()
    return render(request,"mesas/registrar.html", {"frmmesa":frmmesa})

def grabar_m(request):

    if request.method == "POST":
        frmmesa = frmMesa(request.POST)

        if frmmesa.is_valid():
            
            nuevaMesa = Mesa(
                numero=request.POST["numero"],
                estado=request.POST["estado"]
            )
            nuevaMesa.save()

        return redirect('/gestion_mesas/')

    else:
        return redirect('/registrar_mesa/')
    
'''
def editar_m(request, id):
    m = Cliente.objects.get(id=id)
    return render(request,"admin/mesas/actualizar.html", {'m':m})

def actualizar_m(request):
    
    m = Cliente.objects.get(id=request.POST["id"])
    m.numero=request.POST['numero']
    m.dni=request.POST['dni']
    m.save()

    return redirect('/gestion_mesas/')
'''

# CATEGORIAS
def categorias(request):
    lstcategorias = Categoria.objects.all()
    frmcat = frmCategoria()
    return render(request,"categoria/gestionar.html", {"lstcategorias":lstcategorias, "frmcat":frmcat})

def grabarCategoria(request):
    if request.method == "POST":
        frmcat = frmCategoria(request.POST)

        if frmcat.is_valid():
            cd = frmcat.cleaned_data

            nuevaCategoria = Categoria(
                nombre = request.POST["nombre"]
            )
            nuevaCategoria.save()
            print('Se han guardado todos los datos con exito')
            return redirect('/gestion_categorias/')
        
        else:
            print('No se ha podido guardar')
            return redirect('/gestion_categorias/')

# PRODUCTOS
def productos(request):
    lstproductos = Producto.objects.all()
    return render(request,"productos/gestionar.html", {"lstproductos":lstproductos})

def registrar_pr(request):
    #cbxcat = Categoria.objects.all()
    frmprod = frmProducto()
    return render(request,"productos/registrar.html", {"frmprod":frmprod})

def grabar_pr(request):
    
    if request.method=="POST":
        frmprod = frmProducto(request.POST)

        if frmprod.is_valid():
            cd = frmprod.cleaned_data

            nuevoProducto = Producto(
                nombre=request.POST["nombre"],
                categoria=Categoria.objects.get(id=request.POST["categoria"]),
                precio=request.POST["precio"],
                foto=request.FILES["foto"],
                descripcion=request.POST["descripcion"]
            )
            nuevoProducto.save()
            return redirect('/gestion_productos/')  
            
            '''nuevoProducto = Producto.objects.create(
                    nombre=request.POST["nombre"],
                    categoria=Categoria.objects.get(id=request.POST["categoria"]),
                    precio=request.POST["precio"],
                    foto=request.FILES["foto"],
                    descripcion=request.POST["descripcion"]
                )'''
        else:
            print('No se ha podido guardar')
            return redirect('/registrar_productos/')    
            
    #return render(request,"productos/registrar.html", {"frmprod":frmprod})
    

def editar_pr(request, id):
    p = Producto.objects.get(id=id)
    #cbxcat = Categoria.objects.all()
    return render(request,"productos/actualizar.html", 
                  #{"cbxcat":cbxcat}, 
                  {'p':p})

def actualizar_pr(request):
    
    p = get_object_or_404(Producto, id=request.POST.get('id'))

    if request.method == 'POST':
        p.nombre=request.POST.get('nombre')
        p.precio=request.POST.get('precio')
        p.descripcion=request.POST.get('descripcion')
        
        foto=request.FILES.get('foto')
        if foto:
            p.foto = foto

        p.save()

        return redirect('/gestion_productos/')

def eliminar_pr(request, id):

    pr=Producto.objects.get(id=id)

    if pr.estado==True:
        pr.estado=False
        pr.save()
    
    else:
        return redirect('/gestion_productos/')    

    return redirect('/gestion_productos/')

# CLIENTES
def clientes(request):
    lstclientes = Cliente.objects.all()
    return render(request,"clientes/gestionar.html", {"lstclientes":lstclientes})

def registrar_cl(request):
    #return render(request,"admin/clientes/registrar.html")
    formcli = frmCliente(request.POST)
    return render(request,"clientes/registrar.html", {'form':formcli})

def grabar_cl(request):

    if request.method=="POST":

        formcli = frmCliente(request.POST)

        if formcli.is_valid():
            cd = formcli.cleaned_data
            nuevoCliente = Cliente(
                nombre=request.POST["nombre"],
                numero=request.POST["numero"],
                dni=request.POST["dni"]
            )
            nuevoCliente.save()
            
            print('Se han guardado todos los datos con exito')
            return redirect('/gestion_clientes/')

        else:
            print('Error al guardar los datos')
            return redirect('/registrar_cliente/')

    return render(request,"clientes/registrar.html", {'form':formcli})

def editar_cl(request, id):
    cl = Cliente.objects.get(id=id)
    #formcli = frmCliente(instance=cl)
    return render(request,"clientes/actualizar.html", {'cl':cl})

def actualizar_cl(request):
    
    cl = Cliente.objects.get(id=request.POST["id"])
    cl.nombre=request.POST['nombre']
    cl.numero=request.POST['numero']
    cl.dni=request.POST['dni']
    cl.save()

    return redirect('/gestion_clientes/')

def eliminar_cl(request, id):

    try:
        cl=Cliente.objects.get(id=id)

        if cl.estado==True:
            cl.estado=False
            cl.save()
            print('Se desactivo con exito!')
        else:
            print('La propiedad ya está desactivada')
            
        return redirect('/gestion_clientes/') 
     
    except:
        print('No se pudo desactivar')
        lstclientes = Cliente.objects.all()
        return render(request,"clientes/gestionar.html", {"lstclientes":lstclientes})

# ORDENES
def verOrdenes(request):
    lstordenes = Orden.objects.all()
    return render(request,"ordenes/gestionar.html", {"lstordenes":lstordenes})

def editarOrden(request, id):
    o = Orden.objects.get(id=id)
    cbxmesas = Mesa.objects.all()
    lstproductos = Producto.objects.all()
    return render(request,"ordenes/actualizar.html", {'o':o, "cbxmesas":cbxmesas, "lstproductos":lstproductos})

def eliminarOrden(request, id):

    o=Orden.objects.get(id=id)

    if o.estado==True:
        o.estado=False
        o.save()
    
    else:
        return redirect('/gestion_ordenes/')    

    return redirect('/gestion_ordenes/')

'''def registrar_cl(request):
    return render(request,"admin/clientes/registrar.html")

def grabar_cl(request):

    nuevoCliente = Cliente.objects.create(
        nombre=request.POST["nombre"],
        numero=request.POST["numero"],
        dni=request.POST["dni"]
    )

    return redirect('/gestion_clientes/')

def actualizar_cl(request):
    
    cl = Cliente.objects.get(id=request.POST["id"])
    cl.nombre=request.POST['nombre']
    cl.numero=request.POST['numero']
    cl.dni=request.POST['dni']
    cl.save()

    return redirect('/gestion_clientes/')

'''
