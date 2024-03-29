from django_filters import rest_framework as filters
from .models import Estado, Cidade


class EstadoFilter(filters.FilterSet):
    nome = filters.CharFilter(
        field_name='nome', lookup_expr='icontains')

    class Meta:
        model = Estado
        fields = ['nome']


class CidadeFilter(filters.FilterSet):
    nome = filters.CharFilter(
        field_name='nome', lookup_expr='icontains')

    class Meta:
        model = Cidade
        fields = ['nome']
