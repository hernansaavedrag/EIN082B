from django.db import models

class Carrera(models.Model):
    codigo_carrera = models.CharField(max_length=6, primary_key=True, verbose_name="Código")
    nombre = models.CharField(max_length=80, verbose_name="Nombre")
    duracion = models.IntegerField(verbose_name="Duración (semestres)")

    def __str__(self) -> str:
        return self.nombre