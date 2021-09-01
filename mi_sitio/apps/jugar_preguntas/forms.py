from django import forms
from .models import jugar
from apps.preguntas.models import cargar_pregunta, categoria, respuesta_correcta
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


#poner un choice y en el models es  portar todos de una tabla
#import  datetime
class jugarForm(forms.ModelForm):
    #pregunta = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    #pregunta = forms.ChoiceField(choices=[("a","b"),("1","2")],widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    #estado2 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = jugar


        fields = ["puntaje",
                  "estado",
                  "categoria",
                  "cargar_pregunta",
                  #"pregunta",
                  #"respusta_correcta"
                  ]

        labels = {
            "puntaje":"puntajes",
            "estado":"estados",
            "categoria":"categorias",
           # "pregunta":"preguntas",
            "cargar_pregunta": "cargar_preguntas",
            "respuesta_correcta":"respuesta_correcta.respuesta_correcta"
        }

        widget = {
            "puntaje": forms.TextInput(attrs={"class":"form-control"}),
            "estado": forms.TextInput(attrs={"class":"form-control"}),
            "categoria":forms.CheckboxSelectMultiple(attrs={"class":"form-control"}),
           # "pregunta":forms.TextInput(attrs={"class":"form-control"}),
            "cargar_pregunta": forms.SelectMultiple(attrs={"class":"form-control"}),
            "respuesta_correcta": forms.SelectMultiple(attrs={"class":"form-control"}),
        }


        # ver como hacer para que en la pagina jugar aparesca la preguntas y los campos para que eliga el usuario

 #aca ver como hacer para validad lo que el usuario apreta en las pretas
 #creo que aca se tendria que hacer creando la clase clean_"y el nombre del campo que queremos validar"
