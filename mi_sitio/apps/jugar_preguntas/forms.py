"""from django import forms
from .models import jugar, CATEGORIA_CHOICES
from apps.preguntas.models import cargar_pregunta, categoria
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


#poner un choice y en el models es  portar todos de una tabla
#import  datetime
class jugarForm(forms.ModelForm):
    #nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    categoria = forms.ChoiceField(choices=CATEGORIA_CHOICES,widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))

    class Meta:
        model = jugar

        fields = ["puntaje",
            #      "pregunta",
                  "cargar_pregunta",
                  "estado",
                  #"cargar",
                  ]

        labels = {
            "puntaje":"puntajes",
            "cargar_pregunta":"cargar_preguntas",
            "estado":"estados",
           # "pregunta":"preguntas",
            "categoria":"categorias"
        }

        widget = {
            "puntaje": forms.TextInput(attrs={"class":"form-control"}),
            "cargar_pregunta": forms.SelectMultiple(attrs={"class":"form-control"}),
            "estado": forms.TextInput(attrs={"class":"form-control"}),
            #"categoria":forms.CheckboxSelectMultiple(attrs={"class":"form-control"}),
            #"pregunta":forms.TextInput(attrs={"class":"form-control"}),
        }

         ver como hacer para que en la pagina jugar aparesca la preguntas y los campos para que eliga el usuario

 #aca ver como hacer para validad lo que el usuario apreta en las pretas
 #creo que aca se tendria que hacer creando la clase clean_"y el nombre del campo que queremos validar"
"""