from django.contrib.auth.models import User
from http import HTTPMethod
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import mixins
from rest_framework import decorators
from rest_framework import parsers
from rest_framework.response import Response
from .models import Cidade, Estado
from .serializers import (
    CidadeSerializer,
    EstadoSerializer,
    UserSerializer,
    UploadFotoEstadoSerializer)
from .paginations import CustomPagination
from .filters import EstadoFilter, CidadeFilter
from .permissions import IsOwnerOrReadOnly


class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    pagination_class = CustomPagination
    filterset_class = EstadoFilter
    # permission_classes = [
    # permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    parser_classes = [parsers.JSONParser, parsers.MultiPartParser]

    def get_serializer_class(self):
        if self.action not in ['upload_foto']:
            return UploadFotoEstadoSerializer
        return self.serializer_class

    @decorators.action(url_path='upload_foto', detail=True, methods=[HTTPMethod.PUT])
    def upload_foto(self, request, pk):
        estado = Estado.objects.get(pk=pk)
        serializer = UploadFotoEstadoSerializer(
            instance=estado, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(EstadoSerializer(serializer.instance).data)


class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    pagination_class = CustomPagination
    filterset_class = CidadeFilter
    permission_classes = [IsOwnerOrReadOnly]


class SignupAPIView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
