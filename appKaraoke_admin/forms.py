from django import forms
from appKaraoke.models import Cancion, Categoria, Genero, Producto

class frmCliente(forms.Form):
    nombre = forms.CharField()
    dni = forms.CharField()
    numero = forms.CharField(required=False)
    #estado = forms.BooleanField()

class frmCancion(forms.Form):

    nombre = forms.CharField()
    artista = forms.CharField()
    genero = forms.ModelChoiceField(
        queryset=Genero.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = Cancion
        fields = ['nombre', 'artista', 'genero']

class frmProducto(forms.Form):
    nombre = forms.CharField()
    precio = forms.FloatField()
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    foto = forms.ImageField(required=False)
    descripcion = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows':'5', 'cols':'55'})
    )

    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'categoria', 'foto', 'descripcion']

class frmMesa(forms.Form):
    numero = forms.CharField()
    estado = forms.TypedChoiceField(
        choices=((False, "False"), (True, "True")),
        widget=forms.RadioSelect,
    )

class frmCategoria(forms.Form):
    nombre = forms.CharField()

    class Meta:
        model = Categoria
        fields = ['nombre']

class frmGenero(forms.Form):
    nombre = forms.CharField()

    class Meta:
        model = Genero
        fields = ['nombre']