from django.db import models
from apps.jugadores.models import jugadore

class cargar_pregunta(models.Model):
    pregunta = models.CharField(max_length=255)

    class Meta:
        db_table = 'preguntas'

    def __str__(self):
        return self.id, self.pregunta

    def __str__(self):
        return self.pregunta


class cargar_respuesta(models.Model):
    pregunta = models.ForeignKey(cargar_pregunta, on_delete=models.CASCADE,null=True)
    respuesta_correcta = models.CharField(max_length=255)
    respuesta1 = models.CharField(max_length=255)
    respuesta2 = models.CharField(max_length=255)
    respuesta3 = models.CharField(max_length=255)

    class Meta:
        db_table = 'respuestas'

    def __str__(self):
        return self.id, self.pregunta

    def __str__(self):
        return self.pregunta,self.respuesta_correcta,self.respuesta1,self.respuesta2,self.respuesta3


"""class jugador_juega(models.Model):
    jugador = models.ForeignKey(jugadores, on_delete=models.CASCADE)
    cargar_preguntas = models.ForeignKey(cargar_respuestas, on_delete=models.CASCADE)

    class Meta:
        db_table = 'jugador_juega'
"""
