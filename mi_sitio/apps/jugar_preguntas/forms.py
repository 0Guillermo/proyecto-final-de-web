from django import forms
from .models import jugar
from apps.preguntas.models import cargar_pregunta, categoria, respuesta_correcta
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


#poner un choice y en el models es  portar todos de una tabla
#import  datetime
class jugarForm(forms.ModelForm):
    cargar_pregunta = forms.TextInput(attrs={"class": "form-control"})
    estado = forms.CheckboxSelectMultiple(attrs={"class": "form-control"})

    class Meta:
        model = jugar

        fields = [
            "cargar_pregunta",
            "estado",
            ]

        labels = {
            "cargar_pregunta": "cargar_preguntas",
            "estado":"estados",
        }