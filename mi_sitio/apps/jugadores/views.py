from django.shortcuts import render
from .models import jugadore

def lista_de_jugadores (request):
    template_name="participantes/participante.html"
    lista_de_amigos = jugadore.objects.all() # esto es una base de datos
    ctx = {
        'jugador': lista_de_amigos,
    }
    return render(request,template_name, ctx)
# Create your views here.
