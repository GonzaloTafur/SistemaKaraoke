from django.shortcuts import get_object_or_404, redirect, render

from appKaraoke.models import Cancion, Categoria, Cliente, Mesa, Producto

# Create your views here.

def panel_admin(request):
    return render(request, "admin/administracion.html")

def canciones(request):
    lstcanciones = Cancion.objects.all()
    return render(request,"admin/canciones/gestionar.html", {"lstcanciones":lstcanciones})

# MESAS

def mesas(request):
    lstmesas = Mesa.objects.all()
    return render(request,"admin/mesas/gestionar.html", {"lstmesas":lstmesas})

def registrar_m(request):
    lstclientes = Cliente.objects.all()
    return render(request,"admin/mesas/registrar.html", {"lstclientes":lstclientes})
'''
def grabar_m(request):

    numero=request.POST["numero"],
    cliente=Cliente.objects.get(id=request.POST["cliente"]),

    if cliente:
        nuevaMesa = Mesa.objects.create(
            numero=numero,
            cliente=cliente,
            estado=False
        )

    else:
        nuevaMesa = Mesa.objects.create(
            numero=numero,
            estado=True
        )

    return redirect('/gestion_mesas/')

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
    return render(request,"admin/categoria/gestionar.html", {"lstcategorias":lstcategorias})

# PRODUCTOS
def productos(request):
    lstproductos = Producto.objects.all()
    return render(request,"admin/productos/gestionar.html", {"lstproductos":lstproductos})

def registrar_pr(request):
    cbxcat = Categoria.objects.all()
    return render(request,"admin/productos/registrar.html", {"cbxcat":cbxcat})

def grabar_pr(request):

    nuevoProducto = Producto.objects.create(
        nombre=request.POST["nombre"],
        categoria=Categoria.objects.get(id=request.POST["categoria"]),
        precio=request.POST["precio"],
        foto=request.FILES["foto"],
        descripcion=request.POST["descripcion"]
    )

    return redirect('/gestion_productos/')

def editar_pr(request, id):
    p = Producto.objects.get(id=id)
    #cbxcat = Categoria.objects.all()
    return render(request,"admin/productos/actualizar.html", 
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


# CLIENTES
def clientes(request):
    lstclientes = Cliente.objects.all()
    return render(request,"admin/clientes/gestionar.html", {"lstclientes":lstclientes})

def registrar_cl(request):
    return render(request,"admin/clientes/registrar.html")

def grabar_cl(request):

    nuevoCliente = Cliente.objects.create(
        nombre=request.POST["nombre"],
        numero=request.POST["numero"],
        dni=request.POST["dni"]
    )

    return redirect('/gestion_clientes/')

def editar_cl(request, id):
    cl = Cliente.objects.get(id=id)
    return render(request,"admin/clientes/actualizar.html", {'cl':cl})

def actualizar_cl(request):
    
    cl = Cliente.objects.get(id=request.POST["id"])
    cl.nombre=request.POST['nombre']
    cl.numero=request.POST['numero']
    cl.dni=request.POST['dni']
    cl.save()

    return redirect('/gestion_clientes/')