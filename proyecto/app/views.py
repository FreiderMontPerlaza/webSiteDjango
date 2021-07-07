from django.shortcuts import render

from .forms import ContactoForm

# Create your views here.
def home(request):
    return render(request,'app/home.html')

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    return render(request,'app./contacto.html',data)



def galeria(request):
    return render(request,'app/galeria.html')

def manualidades(request):
    return render(request,'app/manualidades.html')
