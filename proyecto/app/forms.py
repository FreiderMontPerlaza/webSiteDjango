from django import forms
from django.db import models
from django  import forms
from django.db.models import fields
from.models import Contactos

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contactos
        fields = '__all__'