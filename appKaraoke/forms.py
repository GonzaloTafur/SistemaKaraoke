from django import forms
from appKaraoke.models import Cancion, MesaCliente, OrdenCancion

class frmOrdenCancion(forms.Form):
    cancion = forms.ModelChoiceField(
        queryset=Cancion.objects.filter(estado=True),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    mesa_cliente = forms.ModelChoiceField(
        queryset=MesaCliente.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = OrdenCancion
        fields = ['cancion', 'mesa_cliente']