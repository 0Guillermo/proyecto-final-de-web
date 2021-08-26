from django.urls import path
from . import views

urlpatterns = [
    path('registrarse/', views.registro_usuario, name="registrarse")
]