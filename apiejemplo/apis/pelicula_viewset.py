from rest_framework import viewsets, serializers, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apiejemplo.apis import GeneroSimpleSerializer, ClasificacionSimpleSerializer
from apiejemplo.models import Pelicula


class PeliculaSerializer(serializers.ModelSerializer):
    clasificacion = ClasificacionSimpleSerializer(read_only=True)
    clasificacion_id = serializers.IntegerField(write_only=True)
    genero = GeneroSimpleSerializer(read_only=True)
    genero_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Pelicula
        fields = '__all__'


class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer

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

    @action(detail=False, methods=['post'], url_path='buscarPelicula')
    def buscar_pelicula(self, request):
        query = request.POST.get('q', '')
        peliculas = Pelicula.objects.filter(nombre__icontains=query)
        serializer = PeliculaSerializer(peliculas, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='buscarGenero')
    def buscar_genero(self, request):
        query = request.POST.get('q', '')
        generos = Pelicula.objects.filter(genero__nombre__icontains=query)
        serializer = PeliculaSerializer(generos, many=True)
        return Response(serializer.data)