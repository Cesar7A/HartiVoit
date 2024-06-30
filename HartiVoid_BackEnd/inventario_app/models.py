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
    descripcion = models.CharField(max_length=350,default='Descripción')
    precio_detal = models.DecimalField(max_digits=20, decimal_places=2)
    precio_mayor = models.DecimalField(max_digits=20, decimal_places=2)
    custom_id = models.CharField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        # Guarda el objeto para asegurarse de que tiene un ID
        if not self.id:
            super(Producto, self).save(*args, **kwargs)
        
        # Genera el custom_id
        if not self.custom_id:
            self.custom_id = f"{self.linea.id:02}{self.proveedor.id:02}{self.id:02}"
        
        super(Producto, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.nombre