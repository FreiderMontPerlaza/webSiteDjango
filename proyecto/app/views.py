from django import contrib
from django.shortcuts import render

from .forms import ContactoForm,productoForm,Producto


# Create your views here.
def home(request):
    return render(request,'app/home.html')

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "se ha guardado los datos correctamente"
        else:
            data["form"] = formulario
    return render(request,'app/contacto.html',data)



def galeria(request):
    return render(request,'app/galeria.html')

def manualidades(request):
    return render(request,'app/manualidades.html')


def agregar_producto(request):

    data = {
        'form':productoForm()
    }

    if request.method == 'POST':
        formulario = productoForm(data=request.POST,files=request.FILES)
        if formulario.is_valid:
            formulario.save()
            data["mensaje"] = "poducto guadado exitosamente"
        else:
            data["form"]= formulario
    return render(request,'app/producto/agregar.html',data)



def listar_producto(request):
    Productos = Producto.objects.all()

    data = {
        'producto':Productos
    }
    return render(request,'app/producto/lista.html',data)