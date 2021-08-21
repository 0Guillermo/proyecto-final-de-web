from django.db import models

class cargar_pregunta(models.Model):
    pregunta = models.CharField(max_length=255)
    respuesta_correcta = models.CharField(max_length=255)
    respuesta1 = models.CharField(max_length=255)
    respuesta2 = models.CharField(max_length=255)
    respuesta3 = models.CharField(max_length=255)

    class Meta:
        db_table = 'preguntas'

    def __str__(self):
        return  self.id, self.pregunta


    def probar_juego(self):
        print(cargar_pregunta.objects.filter("pregunta"))
        print("eliga una opcion")

