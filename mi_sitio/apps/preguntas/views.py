from django.shortcuts import render

from .models import cargar_pregunta, respuesta_correcta#, categoria, respuesta_incorrecta

def lista_de_preguntas (request):
    template_name="preguntas/cargar_preguntas.html"
    lista_de_preguntas = cargar_pregunta.objects.all()
    lista_correctas = respuesta_correcta.objects.all()

#-------------------------
# todo esto no hace naadaa
# ------------------------

    ctx = {
        'pregunta': lista_de_preguntas,
        'respuesta': lista_correctas,

        }
    return  render(request,template_name, ctx)