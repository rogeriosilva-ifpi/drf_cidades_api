from .models import Cidade, Estado
from .serializers import CidadeSerializer, EstadoSerializer
from rest_framework import viewsets
from .paginations import CustomPagination
from .filters import EstadoFilter, CidadeFilter


class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    pagination_class = CustomPagination
    filterset_class = EstadoFilter


class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    pagination_class = CustomPagination
    filterset_class = CidadeFilter
