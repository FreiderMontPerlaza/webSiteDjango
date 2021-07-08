from django.urls import path
from .views import  home,contacto,galeria,manualidades,agregar_producto,listar_productos,modificar_producto,eliminar_producto
urlpatterns = [
    path('',home,name="home"),
    path('contacto/',contacto,name="contacto"),
    path('galeria/',galeria,name="galeria"),
    path('manualidades/',manualidades,name="manualidades"),
    path('agregar-producto/',agregar_producto,name="agregar-producto"),
    path('listar-productos/',listar_productos,name="listar_productos"),
    path('modificar-productos/<id>/',modificar_producto,name="modificar_productos"),
    path('eliminar-producto/<id>/',eliminar_producto,name="eliminar_producto"),

]
