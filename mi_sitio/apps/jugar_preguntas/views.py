from django.shortcuts import render ,redirect
from .models import jugar
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.preguntas.models import cargar_pregunta, respuesta_incorrecta, respuesta_correcta, categoria

from .forms import jugarForm
from apps.estadisticas.forms import EstadisticasForm

def jugar_preg(request):
    template_name = "jugar/jugar_preguntas.html"
    if request.method == "POST":
        forms = jugarForm(request.POST)
        print(forms,"===========================================")
        # if forms.is_valid:
        forms.save()
        return redirect("jugar")
    else:
        forms = jugarForm()

    #
    #ver como hacer para guardar en estadisticas el usuario asosiado a la cuenta
    #en la estadisticas guardar el id del juego
    #y en estado guardar la variable gano o perdio dependiendo que pregunta responde
    #
    #
    cargar = jugar.objects.filter(id=1)
    for a in cargar:
       preg = a.cargar_pregunta.all()
       for b in preg:
           pregunta = b.pregunta
           incorrecta = b.respuesta_incorrecta.all()
           correcta = b.respuesta_correcta.all()
           categ = b.categoria.all()
    long = len(correcta)
    if long < 2:
           long = False
    elif long > 1:
           long = True

    data = {
        'pregunta': pregunta,
        'correcta': correcta,
        'incorrecta': incorrecta,
        "categoria":categ,
        "longitud":long,
        "form": forms,
        #poner un contador
    }
    return render(request,template_name,data)