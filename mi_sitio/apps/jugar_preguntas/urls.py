from django.urls import path
from . import views

app_name = "jugar"

urlpatterns = [
    path('jugar/', views.jugar,name="jugar")
]