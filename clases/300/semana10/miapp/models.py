from django.db import models

class Carrera(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=100)
    duracion = models.IntegerField()

    def __str__(self) -> str:
        return self.nombre

class Docente(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    titulo = models.CharField(max_length=50)
    carrera_id = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre + " " + self.apellido