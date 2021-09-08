from django.db import models
from apps.preguntas.models import cargar_pregunta,  respuesta_correcta, categoria#, respuesta_incorrecta

ESTADOS_CHOICES = (
    ("1","ACTIVO"),
    ("0","INACTIVO"),
)

class jugar(models.Model):
    cargar_pregunta = models.ManyToManyField(cargar_pregunta, related_name="cargar_pregunta")
    estado = models.CharField(max_length=255,choices=ESTADOS_CHOICES,null=True)

    class Meta: 
        db_table = 'jugar'

    def __str__(self):
        return f"{self.cargar_pregunta} {self.estado}"

