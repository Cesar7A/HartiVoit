from django.contrib import admin
from .models import Producto, Linea, Proveedor

# Register your models here.
admin.site.register(Producto)
admin.site.register(Linea)
admin.site.register(Proveedor)