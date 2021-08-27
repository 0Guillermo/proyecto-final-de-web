from django import forms
from django.forms import ModelForm
from .models import jugar,PREGUNTAS_CHOICES
    #import  datetime
from django.contrib.auth.forms import UserCreationForm

class jugarForm(forms.ModelForm):
    cargar_pregunta = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    puntaje = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    estado = forms.ChoiceField(choices=PREGUNTAS_CHOICES, widget=forms.RadioSelect)
    class Meta:
        model = jugar
        fields = ["puntaje","cargar_pregunta"]

        """ ver como hacer para que en la pagina jugar aparesca la preguntas y los campos para que eliga el usuario """

 #aca ver como hacer para validad lo que el usuario apreta en las pretas
 #creo que aca se tendria que hacer creando la clase clean_"y el nombre del campo que queremos validar"