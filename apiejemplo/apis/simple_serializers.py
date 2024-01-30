from rest_framework import serializers
from django.contrib.auth.models import User

from apiejemplo.models import *


class GeneroSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class ClasificacionSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clasificacion
        fields = '__all__'
