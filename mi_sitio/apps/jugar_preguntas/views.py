from django.shortcuts import render

from .models import jugar

def jugar(request):
    template_name="jugar/jugar_preguntas.html"
    opciones = jugar.objects.all()
    ctx = {
        'jugar': opciones,
    }
    return render(request,template_name,ctx)

