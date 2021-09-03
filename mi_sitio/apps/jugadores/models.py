from django.db import models

class jugadore(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    localidad = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255, null=True) #esto va ir en una tabla aparte
    email = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'jugadores'

    def __str__(self):
        return f"{self.id} {self.nombre} {self.apellido} {self.localidad} {self.telefono} {self.email}"

# Create your models here.
