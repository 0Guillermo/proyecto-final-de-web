from django.db import models

class jugadores(models.Model):
    nombre = models.CharField(max_length=255, null=True)
    apellido = models.CharField(max_length=255, null=True)
    localidad = models.CharField(max_length=255, null=True)
    telefono = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'jugadores'

    def __str__(self):
        return self.nombre

# Create your models here.
