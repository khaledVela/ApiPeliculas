from django.urls import path, include
from rest_framework import routers

from apiejemplo.apis import *

router = routers.DefaultRouter()

router.register(r'peliculas', pelicula_viewset.PeliculaViewSet)
router.register(r'generos', genero_viewset.GeneroViewSet)
router.register(r'clasificaciones', clasificacion_viewset.ClasificacionViewSet)
router.register(r'usuarios', usuario_viewset.CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]