from django.db import models
from apps.preguntas.models import cargar_pregunta,  respuesta_correcta, respuesta_incorrecta, categoria

ESTADOS_CHOICES = (
    ("1","ACTIVO"),
    ("0","INACTIVO"),
)

class jugar(models.Model):
    cargar_pregunta = models.ManyToManyField(cargar_pregunta, related_name="cargar_pregunta")
    estado = models.CharField(max_length=255,choices=ESTADOS_CHOICES,null=True)

    # puntaje = models.CharField(max_length=255,null=True)  # si hacierta la preguntas suma alguna clase de puntos

#
#en esta tabla es donde eñ usuario tiene que cargar lo que eligio
#
#

    class Meta: 
        db_table = 'jugar'

    def __str__(self):
        return f"{self.cargar_pregunta} {self.estado}"#{self.puntaje}

