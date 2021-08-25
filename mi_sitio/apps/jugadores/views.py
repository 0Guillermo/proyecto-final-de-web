from django.shortcuts import render
from .models import jugadores

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
#from django.core.urlresolvers import reverse_Lazy

class registrojugador(CreateView):
    model = User
    template_name = "participantes/participante.html"
    form_class = UserCreationForm
    #success_url = reverse_lazy



def lista_de_jugadores (request):
    template_name="participantes/participante.html"
    lista_de_amigos = jugadores.objects.all() # esto es una base de datos
    ctx = {
        'jugador': lista_de_amigos,
    }
    return render(request,template_name, ctx)
# Create your views here.
