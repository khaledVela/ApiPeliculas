from rest_framework import viewsets, serializers, status
from rest_framework.response import Response

from apiejemplo.models import Genero


class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'


class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

    def create(self, request, *args, **kwargs):
        if request.user.tipo == '1':
            return super().create(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, *args, **kwargs):
        if request.user.tipo == '1':
            return super().update(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, *args, **kwargs):
        if request.user.tipo == '1':
            return super().destroy(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)