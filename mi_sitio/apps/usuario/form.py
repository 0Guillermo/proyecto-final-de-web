from django import forms
from django.forms import ModelForm
    #from .models import
    #import  datetime
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    pass

#aca crear un punto de control que si el formulario no cumple los requisitos muestre algun tipo de error