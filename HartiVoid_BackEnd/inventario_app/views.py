from django.shortcuts import render
from rest_framework import viewsets
from .models import Producto, Linea, Proveedor
from .serializers import ProductoSerializer, LineaSerializer, ProveedorSerializer

class LineaViewSet(viewsets.ModelViewSet):
    queryset = Linea.objects.all().order_by('-nombre')
    serializer_class = LineaSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all().order_by('-nombre')
    serializer_class = ProveedorSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('-nombre')
    serializer_class = ProductoSerializer
