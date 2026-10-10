from django.shortcuts import render, redirect, get_object_or_404
from .models import Viaje
from .forms import ViajeForm


def viaje_list(request):
    viajes = Viaje.objects.select_related("viajero", "origen", "destino").all()
    return render(request, "agencia_viajes/viaje_list.html", {"viajes": viajes})


def viaje_create(request):
    form = ViajeForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("av_viaje_list")
    return render(request, "agencia_viajes/viaje_form.html", {"form": form, "accion": "Alta"})


def viaje_update(request, codigo):
    viaje = get_object_or_404(Viaje, codigo=codigo)
    form = ViajeForm(request.POST or None, instance=viaje)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("av_viaje_list")
    return render(request, "agencia_viajes/viaje_form.html", {"form": form, "accion": "Cambio"})


def viaje_delete(request, codigo):
    viaje = get_object_or_404(Viaje, codigo=codigo)
    if request.method == "POST":
        viaje.delete()
        return redirect("av_viaje_list")
    return render(request, "agencia_viajes/viaje_confirm_delete.html", {"viaje": viaje})
