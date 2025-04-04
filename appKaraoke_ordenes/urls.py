from django.urls import path
from appKaraoke_ordenes import views

urlpatterns = [
    path('ordenes/', views.ordenes, name='ordenes'),
    path('grabar_orden/', views.grabarOrden),
    path('lista_ordenes/', views.listaOrdenes, name='lista'),
    path('registrar_mesacliente/', views.registrarMesaCliente, name='registrar_mc'),
    path('grabar_mesacliente/', views.grabarMesaCliente)
]