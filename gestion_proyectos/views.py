from django.shortcuts import render, redirect, get_object_or_404
from .models import Proyecto
from .forms import ProyectoForm


def proyecto_list(request):
    proyectos = Proyecto.objects.select_related("cliente").all()
    return render(request, "gestion_proyectos/proyecto_list.html", {"proyectos": proyectos})


def proyecto_create(request):
    form = ProyectoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("gp_proyecto_list")
    return render(request, "gestion_proyectos/proyecto_form.html", {"form": form, "accion": "Alta"})


def proyecto_update(request, codigo):
    proyecto = get_object_or_404(Proyecto, codigo=codigo)
    form = ProyectoForm(request.POST or None, instance=proyecto)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("gp_proyecto_list")
    return render(request, "gestion_proyectos/proyecto_form.html", {"form": form, "accion": "Cambio"})


def proyecto_delete(request, codigo):
    proyecto = get_object_or_404(Proyecto, codigo=codigo)
    if request.method == "POST":
        proyecto.delete()
        return redirect("gp_proyecto_list")
    return render(request, "gestion_proyectos/proyecto_confirm_delete.html", {"proyecto": proyecto})
