from django.urls import path
from . import views

app_name = "jugadores"

urlpatterns = [
    path('jugadores/', views.lista_de_jugadores, name="jugadores")
]