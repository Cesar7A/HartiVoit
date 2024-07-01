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
    linea = serializers.PrimaryKeyRelatedField(queryset=Linea.objects.all())
    proveedor = serializers.PrimaryKeyRelatedField(queryset=Proveedor.objects.all())

    linea_nombre = serializers.SlugRelatedField(source='linea', slug_field='nombre', read_only=True)
    proveedor_nombre = serializers.SlugRelatedField(source='proveedor', slug_field='nombre', read_only=True)

    class Meta:
        model = Producto
        fields = '__all__'
        

    def create(self, validated_data):
        Producto(**validated_data).save()
        return Producto.objects.get(**validated_data)

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.cantidad = validated_data.get('cantidad', instance.cantidad)
        instance.marca = validated_data.get('marca', instance.marca)
        instance.linea = validated_data.get('linea', instance.linea)
        instance.proveedor = validated_data.get('proveedor', instance.proveedor)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.precio_detal = validated_data.get('precio_detal', instance.precio_detal)
        instance.precio_mayor = validated_data.get('precio_mayor', instance.precio_mayor)
        instance.save()
        return instance