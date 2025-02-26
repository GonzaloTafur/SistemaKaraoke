from django.urls import path
from appKaraoke import views

urlpatterns = [
    path('', views.login),
    path('principal/', views.principal),
    path('dj/', views.dj),
    path('grabarCancion/', views.grabar_cancion)
]
