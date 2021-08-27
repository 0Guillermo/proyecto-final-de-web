from django.db import models
from apps.preguntas.models import cargar_pregunta

PREGUNTAS_CHOICES = (
    ("A","ALGO"),
    ("B"," PREGUNTASSS")
)

class jugar(models.Model):
    cargar_pregunta = models.ForeignKey(cargar_pregunta, on_delete=models.CASCADE,null=True)
    puntaje = models.CharField(max_length=255,null=True) #esto tiene que ser un metodo creo.
                                                         # si hacierta la preguntas suma alguna clase de puntos

    class Meta: 
        db_table = 'jugar'

    def __str__(self):
        return f"{self.cargar_pregunta} {self.puntaje}"

# cargar un objeto de preguntas para que despues se pueda exporta a la carpeta views
# donde se tendra acceso para que se pueda ver en la pagina