from django.urls import path
from appKaraoke import views

urlpatterns = [
    path('', views.login),
    #path('principal/', views.principal),
    path('dj/', views.dj),
    path('grabar_orden_cancion/', views.grabar_cancion),
    path('eliminar_orden_cancion/<id>', views.eliminarOrdenCancion, name="eliminar_oc")
]
