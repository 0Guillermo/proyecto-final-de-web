from django.shortcuts import render ,redirect
from .models import jugar
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.preguntas.models import cargar_pregunta, respuesta_incorrecta, respuesta_correcta, categoria

from .forms import jugarForm

def jugar_preg(request):
    template_name = "jugar/jugar_preguntas.html"
    if request.method == "POST":
        forms = jugarForm(request.POST)
        forms.save()
        return redirect("jugar")
    else:
        forms = jugarForm()

    data = {
        "form":forms,
    }

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