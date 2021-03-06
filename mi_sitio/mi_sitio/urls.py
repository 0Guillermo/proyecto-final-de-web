from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio,name="inicio"),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', auth_views.logout_then_login, name="logout"),
    path('inicio/',include('apps.usuario.urls'),name="registrarse"),
    path('inicio/',include('apps.jugar_preguntas.urls'),name="jugar"),
    path('inicio/',include('apps.estadisticas.urls'),name="estadisticas"),

    # ver como unir al usuario con el jugador!!!!!!
    path('inicio/',include('apps.jugadores.urls'),name="jugadores"),


    path('admin/',include('apps.preguntas.urls')),

]
