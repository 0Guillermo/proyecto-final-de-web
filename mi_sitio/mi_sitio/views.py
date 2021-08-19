from django.shortcuts import  render
def inicio(request):
    template_name="inicio.html"
    lista_almunos=[
        "alumno 1",
        "alumno 2"
    ]                                         #ESTA ES LA PAGUINA INICIO MODIFICAR!!!!!
    ctx = {
        "username":"guillermo",
        "lista":lista_almunos
    }
    return render(request,template_name, ctx)