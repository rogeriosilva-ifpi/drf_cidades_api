from rest_framework.serializers import ModelSerializer
from core.models import Cidade, Estado


class CidadeSerializer(ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'


class EstadoSerializer(ModelSerializer):
    cidades = CidadeSerializer(many=True, read_only=True)

    class Meta:
        model = Estado
        fields = ['id', 'nome', 'sigla', 'cidades']
