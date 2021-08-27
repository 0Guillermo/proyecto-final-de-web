from django.shortcuts import render
from .models import jugar
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import jugarForm

"""class EnpezarJugar(CreateView):
    model = jugar
    template_name = "jugar/jugar_preguntas.html"
    form_class = jugarForm

    def get_success_url(self, **kwargs):
        return reverse_lazy("inicio")

lo que esta arriba usar eso para guardar los datos del perfil del usario una ves que se registra pedirle los datos para el perfil

"""


def jugar_preg(request):
    template_name="jugar/jugar_preguntas.html"
    #opciones = jugar.objects.all()
    opciones="guille"
    ctx = {
        'jugar': opciones,
    }
    return render(request,template_name,ctx)
