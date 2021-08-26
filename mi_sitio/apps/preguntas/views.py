from django.shortcuts import render

from .models import cargar_pregunta, cargar_respuesta

def lista_de_preguntas (request):
    template_name="preguntas/cargar_preguntas.html"
    lista_de_preguntas = cargar_pregunta.objects.all()
    lista_de_respuestas = cargar_respuesta.objects.all()
    # aca crear puntos de control que cargar un objeto de la clase cargar pregunta
    # y que las preguntas no sean repetidas para el mismo usuario
    # tambien que una ves que respondio toodas las preguntas disponible en la base vuelva a empezar o sea que puede volver a responder las preguntas repetidas

    ctx = {
        'pregunta': lista_de_preguntas,
        'respuesta': lista_de_respuestas,
    }
    return  render(request,template_name, ctx)