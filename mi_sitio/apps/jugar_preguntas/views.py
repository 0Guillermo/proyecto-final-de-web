from django.shortcuts import render
from .models import jugar

def jugar(request):
    template_name = "jugar/jugar.html"
    lista_de_preguntas = ["hola","holaaa"]#aca tiene que estar la clase jugar creo, para cargar en el variable 'preguntas'
                                          # para usarlo en el archivo html y asi poder ver las preguntas en la paguina...
    ctx = {
        'preguntas': lista_de_preguntas,
    }
    return render(request, template_name, ctx)
# Create your views here.
