from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .viewsets import EstadoViewSet, CidadeViewSet

# Roteador raiz para /estados
router = DefaultRouter()
router.register(r'estados', EstadoViewSet)

estado_router = routers.NestedDefaultRouter(
    router, r'estados', lookup='estado')
estado_router.register(r'cidades', CidadeViewSet,
                       basename='estado-cidades')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(estado_router.urls)),
]
