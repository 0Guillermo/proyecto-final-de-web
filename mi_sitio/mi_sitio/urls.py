from django.contrib import admin
from django.urls import path, include
from .views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio),
    path('admin/',include('apps.jugadores.urls')),
    path('admin/',include('apps.jugar_preguntas.preguntas.urls')),
]
