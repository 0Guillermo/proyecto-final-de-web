from django.shortcuts import render, redirect
from .form import UserForm
from django.contrib.auth import login, authenticate

def registro_usuario(request):
    template_name = "registrarse.html"
    data = {
        "form":UserForm()
    }
    if request.method == "POST":
        formulario = UserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #una ves que se autentica el usuario redirigirlo al inicio
            username = formulario.cleaned_data["username"]
            password = formulario.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to="inicio")
    return render(request,template_name,data)