from django.shortcuts import render

from .preguntas.models import cargar_pregunta

class jugar(models.Model):
    lista_de_amigos = cargar_preguntas.objects.all()
    ctx = {
        'jugador': lista_de_amigos,
    }
# Create your views here.
