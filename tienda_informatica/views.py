from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm


def producto_list(request):
    productos = Producto.objects.all()
    return render(request, "tienda_informatica/producto_list.html", {"productos": productos})


def producto_create(request):
    form = ProductoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ti_producto_list")
    return render(request, "tienda_informatica/producto_form.html", {"form": form, "accion": "Alta"})


def producto_update(request, codigo):
    producto = get_object_or_404(Producto, codigo=codigo)
    form = ProductoForm(request.POST or None, instance=producto)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ti_producto_list")
    return render(request, "tienda_informatica/producto_form.html", {"form": form, "accion": "Cambio"})


def producto_delete(request, codigo):
    producto = get_object_or_404(Producto, codigo=codigo)
    if request.method == "POST":
        producto.delete()
        return redirect("ti_producto_list")
    return render(request, "tienda_informatica/producto_confirm_delete.html", {"producto": producto})
