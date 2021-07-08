from.views import contacto
from django.contrib import admin
from.models import Contactos,Marca,Producto

# Register your models here.

class productoAmin(admin.ModelAdmin):
    list_display = ["nombre","precio","disponible","marca"] #agrego mas columnas
    list_editable = ["precio"]  # poder editar la columna precio
    search_fields =["nombre"] # busqueda por nombre
    list_filter = ["marca","disponible"] # filtro por la marca o si esta disponible o no
    

admin.site.register(Marca)
admin.site.register(Producto,productoAmin)
admin.site.register(Contactos)
