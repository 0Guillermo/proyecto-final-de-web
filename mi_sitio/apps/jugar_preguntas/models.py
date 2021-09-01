from django.db import models
from apps.preguntas.models import cargar_pregunta,  respuesta_correcta, respuesta_incorrecta, categoria

ESTADOS_CHOICES = (
    ("1","ACTIVO"),
    ("0","INACTIVO"),
)

class jugar(models.Model):
    cargar_pregunta = models.ManyToManyField(cargar_pregunta, related_name="cargar_pregunta")
    puntaje = models.CharField(max_length=255,null=True) #esto tiene que ser un metodo creo.
    estado = models.CharField(max_length=255,choices=ESTADOS_CHOICES,null=True) # si hacierta la preguntas suma alguna clase de puntos
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE, null=True)


    class Meta: 
        db_table = 'jugar'

    def __str__(self):
        return f"{self.cargar_pregunta} {self.puntaje}{self.estado}"

