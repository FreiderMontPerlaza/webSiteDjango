from django import contrib
from django.shortcuts import render,redirect,get_object_or_404

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



def listar_productos(request):
    product = Producto.objects.all

    data = {
        'product':product
    }
    return render(request,'app/producto/listar.html',data)



def modificar_producto(request,id):

    prodct = get_object_or_404(Producto, id = id )
    data = {
        'form':productoForm(instance=prodct) 
    }
    if request.method == 'POST':
        formulario = productoForm(data = request.POST, instance=prodct, files=request.FILEs)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_productos")
        data["form"] = formulario
    return render(request, 'app/producto/modificar.html',data)

def eliminar_producto(request,id):
    product = get_object_or_404(Producto,id=id)
    product.delete()
    return redirect(to="listar_productos")