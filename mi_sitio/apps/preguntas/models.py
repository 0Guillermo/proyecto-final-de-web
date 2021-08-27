from django.db import models
from apps.jugadores.models import jugadore

class categoria(models.Model):
    categoria_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'categorias'

    def __str__(self):
        return f"id{self.id}: {self.categoria_name}"


class respuesta_correcta(models.Model):
    respuesta_correcta = models.CharField(max_length=255)

    class Meta:
        db_table = 'respuesta_correcta'

    def __str__(self):
        return f"id {self.id}): {self.respuesta_correcta}"

class respuesta_incorrecta(models.Model):

    respuesta_incorrecta = models.CharField(max_length=255)

    class Meta:
        db_table = 'respuesta_incorrecta'

    def __str__(self):
        return f"id {self.id}: {self.respuesta_incorrecta}"

class cargar_pregunta(models.Model):
    pregunta = models.CharField(max_length=255)
    categoria = models.ManyToManyField(categoria, related_name="categoria")
    respuesta_correcta = models.ManyToManyField(respuesta_correcta, related_name="respuesta_correctas")
    respuesta_incorrecta = models.ManyToManyField(respuesta_incorrecta, related_name="respuesta_incorrectas")

    class Meta:
        db_table = 'preguntas'

    def __str__(self):
        return f"{self.id}): {self.pregunta}"

"""class jugador_juega(models.Model):
    jugador = models.ForeignKey(jugadores, on_delete=models.CASCADE)
    cargar_preguntas = models.ForeignKey(cargar_respuestas, on_delete=models.CASCADE)

    class Meta:
        db_table = 'jugador_juega'
        
    ver como hacer esto para que el jugador acceda a esta preguntas
    pero creo que esto tiene ue estar cargado en la apps jugar_preguntas!!!!!!!!!!
        
"""
