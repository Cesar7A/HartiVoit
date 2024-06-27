from rest_framework import serializers
from .models import Producto, Linea, Proveedor

class LineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Linea
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    linea = LineaSerializer()
    proveedor = ProveedorSerializer()

    class Meta:
        model = Producto
        fields = '__all__'