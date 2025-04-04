from django import forms
from appKaraoke.models import Cliente, Mesa, MesaCliente, Orden, Producto

class frmOrden(forms.ModelForm):
    mesa_cliente = forms.ModelChoiceField(
        queryset=MesaCliente.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    total = forms.FloatField()
    producto = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, 
        queryset=Producto.objects.all()
    )

    class Meta:
        model = Orden
        fields = ['mesa_cliente', 'total', 'producto']

class frmMesaCliente(forms.Form):
    mesa = forms.ModelChoiceField(
        queryset=Mesa.objects.filter(estado=True),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.filter(estado=True),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = MesaCliente
        fields = ['mesa', 'cliente']