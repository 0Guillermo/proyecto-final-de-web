from django.urls import path
from . import views

urlpatterns = [
    path('jugar/<int:opcion>', views.jugar_preg,name="jugar"),
    path('jugar/', views.jugar_preg,name="ajugar")
]
