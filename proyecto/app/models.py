from django.db import models

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

    def __str__(self):
        return self.nombre
