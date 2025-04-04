
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from appKaraoke_admin import views

urlpatterns = [
    path('principal/', views.panel_admin, name="principal"),

    path('gestion_mesas/', views.mesas, name="mesas"),
    path('registrar_mesa/', views.registrar_m, name="registrar_m"),
    path('grabar_mesa/', views.grabar_m),
    #path('editar_mesa/<id>',views.editar_m, name="editar_m"),
    #path('actualizar_mesa/', views.actualizar_m),

    path('gestion_canciones/', views.canciones, name="canciones"),
    path('registrar_cancion/', views.registrarCancion, name="registrar_ca"),
    path('grabar_cancion/', views.grabarCancion),
    path('editar_cancion/<id>',views.editar_ca, name="editar_ca"),
    path('actualizar_cancion/', views.actualizar_ca),
    path('eliminar_cancion/<id>',views.eliminar_ca, name="eliminar_ca"),

    path('gestion_generos/', views.generos, name="generos"),
    path('grabar_genero/', views.grabarGenero),

    path('gestion_categorias/', views.categorias, name="categorias"),
    path('grabar_categoria/', views.grabarCategoria),
    
    path('gestion_productos/', views.productos, name="productos"),
    path('registrar_productos/', views.registrar_pr, name="registrar_pr"),
    path('grabar_producto/', views.grabar_pr),
    path('editar_producto/<id>',views.editar_pr, name="editar_pr"),
    path('actualizar_producto/', views.actualizar_pr),
    path('eliminar_producto/<id>',views.eliminar_pr, name="eliminar_pr"),

    path('gestion_clientes/', views.clientes, name="clientes"),
    path('registrar_cliente/', views.registrar_cl, name="registrar_cl"),
    path('grabar_cliente/', views.grabar_cl),
    path('editar_cliente/<id>',views.editar_cl, name="editar_cl"),
    path('actualizar_cliente/',views.actualizar_cl),
    path('eliminar_cliente/<id>',views.eliminar_cl, name="eliminar_cl"),

    path('gestion_ordenes/',views.verOrdenes, name="ver_ordenes"),
    path('editar_orden/<id>',views.editarOrden, name="editar_o"),
    path('eliminar_orden/<id>',views.eliminarOrden, name="eliminar_o"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)