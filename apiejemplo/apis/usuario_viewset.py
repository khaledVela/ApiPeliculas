from django.contrib.auth.hashers import make_password
from rest_framework import viewsets, serializers, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apiejemplo.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    # permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        if request.user.tipo == '1':
            return super().list(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def create(self, request, *args, **kwargs):
        CustomUser.objects.create_user(password=request.data['password'],
                                       email=request.data['email'],
                                       first_name=request.data['first_name'],
                                        last_name=request.data['last_name'],
                                       tipo=request.data['tipo'],
                                       username=request.data['username'],
                                       is_active=True,
                                       carnet=request.data['carnet'])
        return Response(status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        if request.user.id == kwargs['pk'] or request.user.tipo == '1':
            if request.data.get('password'):
                _mutable = request.data._mutable
                request.data._mutable = True
                # Obtener la contraseña proporcionada por el usuario
                password = request.data.get('password')
                tipo = CustomUser.objects.get(id=kwargs['pk']).tipo

                # Encriptar la contraseña usando make_password
                hashed_password = make_password(password)

                # Actualizar la solicitud con la contraseña encriptada
                request.data['password'] = hashed_password
                request.data['tipo'] = tipo
                request.data._mutable = _mutable
            return super().update(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, *args, **kwargs):
        if (request.user.tipo == '1' or request.user.id == kwargs['pk']):
            return super().destroy(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
