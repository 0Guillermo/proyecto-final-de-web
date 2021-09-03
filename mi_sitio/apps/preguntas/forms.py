from apps.preguntas.models import cargar_pregunta
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class preguntaForm(forms.ModelForm):
    pregunta = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    categoria = forms.CharField(choices=[("a","b"),("1","2")],widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    respuesta_incorrecta = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-check-input'}))
    respuesta_correcta = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = cargar_pregunta

        fields = [
            "pregunta",
            "categoria",
            "respuesta_incorrecta",
            "respuesta_correcta",
            #"pregunta",
            #"respusta_correcta"
                  ]

        labels = {
            "pregunta":"pregunta",
            "categoria":"categorias",
            "respuesta_incorrecta": "respuesta_incorrecta",
            "respuesta_correcta":"respuesta_correctas",
            #"cargar_pregunta": "cargar_preguntas",
            # "pregunta":"preguntas",
        }
"""
        widget = {
            "puntaje": forms.TextInput(attrs={"class":"form-control"}),
            "estado": forms.TextInput(attrs={"class":"form-control"}),
            "categoria":forms.CheckboxSelectMultiple(attrs={"class":"form-control"}),
           # "pregunta":forms.TextInput(attrs={"class":"form-control"}),
            "cargar_pregunta": forms.SelectMultiple(attrs={"class":"form-control"}),
            "respuesta_correcta": forms.SelectMultiple(attrs={"class":"form-control"}),
        }
"""