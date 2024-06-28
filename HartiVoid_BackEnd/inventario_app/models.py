from django.db import models

# Create your models here.

class Linea(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    marca = models.CharField(max_length=100)
    linea = models.ForeignKey(Linea, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    precio_detal = models.DecimalField(max_digits=20, decimal_places=2)
    precio_mayor = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.nombre