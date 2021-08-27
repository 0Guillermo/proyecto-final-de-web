from django.urls import path
from . import views

urlpatterns = [
    path('jugar/', views.EnpezarJugar,name="jugar")
]