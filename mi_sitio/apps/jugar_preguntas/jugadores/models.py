from django.db import models

class jugadores (models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    localidad = models.CharField(max_length=255)

    class Meta:
        db_table = 'jugadores'

    def __str__(self):
        return self.nombre

# Create your models here.
