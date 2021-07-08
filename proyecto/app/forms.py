from django import forms
from django.db import models
from django  import forms
from django.db.models import fields
from django.forms import widgets
from.models import Contactos,Producto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = '__all__'



class productoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

widgets = {
    "fecha_fabricacion":forms.SelectDateWidget()
}
   