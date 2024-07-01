from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Producto, Linea, Proveedor
from .serializers import ProductoSerializer, LineaSerializer, ProveedorSerializer

class LineaViewSet(viewsets.ModelViewSet):
    queryset = Linea.objects.all().order_by('nombre')
    serializer_class = LineaSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all().order_by('nombre')
    serializer_class = ProveedorSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('custom_id')
    serializer_class = ProductoSerializer

class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer