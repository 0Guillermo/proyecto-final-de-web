from django.db import models
from .preguntas.models import cargar_pregunta
from .jugadores.models import jugadores

"""ver como hacer para que la clase #jugar# hedere la las calse jugador y la clase preguntas
para que un jugador respondas las preguntas
"""

class jugar(models.Model):
   opcion = models.CharField(max_length=255)

   class Meta:
      db_table = 'jugar'

   def __str__(self):
      return self.id, self.opcion



"""def probar_juego(self):
      print(cargar_pregunta.objects.filter("pregunta"))
      print("eliga una opcion")
"""
## ver bien como cargar las preguntas
## hacer pintos de control para que dependiendo la pregunta que eliga diga si es corerecto o no