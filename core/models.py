from django.db import models


class Estado(models.Model):
    nome = models.CharField(max_length=128, null=False, blank=False)
    sigla = models.CharField(max_length=2, null=False, blank=False)


class Cidade(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    estado = models.ForeignKey(
        Estado, on_delete=models.CASCADE, related_name='cidades')
