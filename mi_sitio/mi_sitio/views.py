from django.shortcuts import  render
from django.contrib.auth.models import User

def inicio(request):
    template_name="inicio.html"
    lista=[ "usuario"
    ]                                         #ESTA ES LA PAGUINA INICIO MODIFICAR!!!!!
    ctx = {
        "lista":lista
    }
    return render(request,template_name, ctx)