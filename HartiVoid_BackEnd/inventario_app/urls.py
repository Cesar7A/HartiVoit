from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, LineaViewSet, ProveedorViewSet, ProductoListCreateView, ProductoDetailView

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'lineas', LineaViewSet)
router.register(r'proveedores', ProveedorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('productos/', ProductoListCreateView.as_view(), name='producto-list-create'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='producto-detail'),
]