from django.shortcuts import render
from rest_framework import viewsets
from .models import Producto, Linea, Proveedor
from .serializers import ProductoSerializer, LineaSerializer, ProveedorSerializer
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class LineaViewSet(viewsets.ModelViewSet):
    queryset = Linea.objects.all().order_by('nombre')
    serializer_class = LineaSerializer
    permission_classes = [DjangoModelPermissions]

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all().order_by('nombre')
    serializer_class = ProveedorSerializer
    permission_classes = [DjangoModelPermissions]

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('custom_id')
    serializer_class = ProductoSerializer
    permission_classes = [DjangoModelPermissions]

class UserPermissionsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        permissions = {
            "can_edit": user.has_perm('inventario_app.change_producto'),
            "can_delete": user.has_perm('inventario_app.delete_producto'),
            "can_create": user.has_perm('inventario_app.add_producto'),
        }
        return Response(permissions)