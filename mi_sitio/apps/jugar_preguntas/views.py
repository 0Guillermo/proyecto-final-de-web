"""from django.shortcuts import render ,redirect
from .models import jugar
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import jugarForm

def jugar_preg(request):
   template_name = "jugar/jugar_preguntas.html"
   if request.method == "POST":
      form = jugarForm(request.POST)
      if form.is_valid():
          form.save()
      return redirect("inicio")
   else:
       form = jugarForm()

   data = {
        "form":form,

   }
   return render(request,template_name,data)
"""