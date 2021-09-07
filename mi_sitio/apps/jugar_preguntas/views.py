from django.shortcuts import render ,redirect
from .models import jugar
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.preguntas.models import cargar_pregunta, respuesta_incorrecta, respuesta_correcta, categoria

from .forms import jugarForm
from apps.estadisticas.forms import EstadisticasForm
import random
# cuando en opcion se cargue 1 o 0 se haga un save de estadisticas cargando si gano o perdio y el punto acumulado

#EN ESTA LISTA CARGAR TODA LAS LISTA DE LAS ID JUGAR
    # PARA QUE A UN USUARIO NO LE VUELVA A REETIR LAS PREGUNTAS QUE YA JUGO

    #EN NIVEL SUMAR UN PUNTOS SI SE ACERTO LA PREGUNTA
    # SI NO SE ACERTO LA PREGUNTA NO SUMAR NADA Y HACER OTRA PREGUNTA

    #HACER ME MUESTRE UN MSJ DE RESUESTA INCORRECTA Y DE RESPUESTA CORRECTA
    # HACER QUE SI TARDA MAS DE 30 SEGUNDO EN RESPONDER LA PREGUNTA LOS PUNTOS SE DIVIDAN A LA MITAD

    #SI ALCANZA HACER QUE LAS REGUNTAS INCORRECTAS SE CARGEN EN UN OTRO COMPO DE LA TABLA
    # PARA QUE UNA VES QUE RESPONDA TODAS LAS PREGUNTAS DISPONIBLE PUEDA JUGAR LAS PREGUNTAS INCORRECTAS

    #PONER UN NUEVO ATRIUTOS EN LA TABLA ESTADISTICAS QUE GUARDE EL ID DE LAS PREGUNTAS JUGADAS

    # hacer una funcion de que si el id que busca no existe que sigo con otra ide


lista = []

def jugar_preg(request,opcion=None):
    template_name = "jugar/jugar_preguntas.html"
    print(opcion,"zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
    #print(lista,"¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿")
    total_preg = jugar.objects.all() #esto poner que se guarde en una variable y una funcion para que solo pregunte una sola ves
    a = len(total_preg)
    while True:
        valor = int(random.random() * a+1)
        print(valor,"wwwwwwwwwwwwwwwwwwwwww")
       # print(a,len(lista),"'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
        if a == len(lista):
            lista1 = []
            
            ## aca poner algo para que una ves que responda todas las preguntas disponibles diga algun msj de final 
            ## y que aprete tal boton para para volver a jugar 
            
            break
        elif valor not in lista:
            lista.append(valor)
            print(lista,"lkisaoaooooooooooooooooooooooooooooooooooooooooooooooo")
            break

    cargar = jugar.objects.filter(id=valor)
    lista_de_preguntas = []
    for a in cargar:
       preg = a.cargar_pregunta.all()
       for b in preg:
           pregunta = b.pregunta
           incorrecta = b.respuesta_incorrecta.all()
           print(incorrecta,"7777777777777777777777777777777")
           correcta = b.respuesta_correcta.all()
           categ = b.categoria.all()
    long = len(correcta)

    print(correcta,"#######################################")
    print(b,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    
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
        "total_preg":lista_de_preguntas,
        #poner un contador
    }
    return render(request,template_name,data)
