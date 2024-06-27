from django.shortcuts import render
from rest_framework import viewsets
from .models import Producto, Linea, Proveedor
from .serializers import ProductoSerializer, LineaSerializer, ProveedorSerializer

class LineaViewSet(viewsets.ModelViewSet):
    queryset = Linea.objects.all()
    serializer_class = LineaSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
