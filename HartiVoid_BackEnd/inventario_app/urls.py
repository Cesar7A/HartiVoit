from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, LineaViewSet, ProveedorViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'lineas', LineaViewSet)
router.register(r'proveedores', ProveedorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]