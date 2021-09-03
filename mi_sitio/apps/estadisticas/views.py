from django.shortcuts import render, redirect
from apps.jugar_preguntas.models import jugar
from apps.estadisticas.models import estadisticas
from apps.jugar_preguntas.forms import jugarForm
from apps.estadisticas.forms import EstadisticasForm
from apps.preguntas.models import cargar_pregunta
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

def EstadisticasViews(request):
    template_name = "jugar/jugar_preguntas.html"
    if request.method == "POST":
        forms = jugarForm(request.POST)
        print(forms, "0000000000000000000")
        if forms.is_valid:
            forms.save()
        return redirect("jugar")
    else:
        forms = jugarForm()

    cargar = jugar.objects.filter(id=2)
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
        "categoria": categ,
        "longitud": long,
        "cargar":cargar,
        "form": forms,
        # poner un contador
    }
    return render(request,template_name,data)

