from django.db import models
from apiejemplo.models import Genero, Clasificacion


class Pelicula(models.Model):
    nombre = models.CharField(max_length=50)
    portada = models.ImageField(upload_to='peliculas/', null=True, blank=True)
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.CASCADE, related_name='clasificacion')
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name='genero')
    fecha_estreno = models.DateField()
    sinonpsis = models.CharField(max_length=500)

    def __str__(self):
        return self.titulo
