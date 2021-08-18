from django.shortcuts import render

from .models import jugadores

def lista_de_jugadores (request):
    template_name="participantes/participante.html"
    lista_de_amigos = jugadores.objects.all()
    ctx = {
        'jugador': lista_de_amigos, # la keys amigos va estar disponible para usar en el archivo HTMl puede ser cualquier cosa esta keys
    }
    return  render(request,template_name, ctx)
# Create your views here.
