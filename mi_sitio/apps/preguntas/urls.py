from django.urls import path

from . import views

app_name = "pregunta"

urlpatterns = [
    path('cargar/', views.lista_de_preguntas)
]