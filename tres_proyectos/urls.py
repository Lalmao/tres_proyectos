from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("gestion-proyectos/", include("gestion_proyectos.urls")),
    path("tienda-informatica/", include("tienda_informatica.urls")),
    path("agencia-viajes/", include("agencia_viajes.urls")),
]
