from rest_framework import viewsets, serializers, status
from rest_framework.response import Response

from apiejemplo.models import Clasificacion


class ClasificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clasificacion
        fields = '__all__'


class ClasificacionViewSet(viewsets.ModelViewSet):
    queryset = Clasificacion.objects.all()
    serializer_class = ClasificacionSerializer

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