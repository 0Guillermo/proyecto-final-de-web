from apps.estadisticas.models import estadisticas
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms

class EstadisticasForm(forms.ModelForm):
    participante = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    juegos = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    estado = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = estadisticas

        fields = ["participante",
                  "juegos",
                  "estado",
                  ]

        labels = {
            "participante":"participantes",
            "juegos":"juegos",
            "estado":"estados",
        }