from django.db import models

class jugadore(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    localidad = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'jugadores'

    def __str__(self):
        return self.nombre

# Create your models here.
