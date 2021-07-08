from django.urls import path
from .views import  home,contacto,galeria,manualidades,agregar_producto,listar_producto

urlpatterns = [
    path('',home,name="home"),
    path('contacto/',contacto,name="contacto"),
    path('galeria/',galeria,name="galeria"),
    path('manualidades/',manualidades,name="manualidades"),
    path('agregar-producto/',agregar_producto,name="agregar-producto"),
    path('listar-producto/',listar_producto,name='listar_productos'),


]
