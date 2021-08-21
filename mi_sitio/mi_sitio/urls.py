from django.contrib import admin
from django.urls import path, include
from .views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/',include('apps.jugar_preguntas.jugadores.urls')),
    path('admin/',include('apps.jugar_preguntas.preguntas.urls')),
    path('inicio/', inicio),
    path('inicio/', include('apps.jugar_preguntas.urls')),
]
