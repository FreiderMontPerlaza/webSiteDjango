from django.contrib import admin
from django.db import models
from django.db.models.query_utils import RegisterLookupMixin
from django.shortcuts import render

# Create your models here.
class Marca(models.Model):
    marca = models.CharField(max_length=50)

class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    precio = models.IntegerField()
    descripcion = models.TextField()
    disponible = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete= models.PROTECT)
    fecha_creacion = models.DateField()
    imagen = models.ImageField(upload_to = "producto",null = True)

    def __str__(self):
        return self.nombre 




opciciones_consulta = [
    [0,"consulta"],
    [1,"reclamo"],
    [2,"sugerencia"],
    [3,"felicitaciones"]
]

#modelo contacto
class Contactos(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciciones_consulta)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return  self.nombre

