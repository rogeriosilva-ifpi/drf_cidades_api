from rest_framework import serializers
from core.models import Cidade, Estado
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'


class EstadoSerializer(serializers.ModelSerializer):
    cidades = CidadeSerializer(many=True, read_only=True)
    foto = serializers.ImageField(read_only=True)

    class Meta:
        model = Estado
        fields = ['id', 'nome', 'sigla', 'foto', 'cidades']


class UploadFotoEstadoSerializer(serializers.ModelSerializer):

    foto = serializers.ImageField(required=True)

    class Meta:
        model = Estado
        fields = ['foto']
