from django.contrib import admin
from .models import Cliente, Proveedor, Producto, ProductoProveedor, Compra


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre", "apellidos", "telefono", "direccion")
    search_fields = ("codigo", "nombre", "apellidos")


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre", "apellidos", "provincia", "telefono")
    search_fields = ("codigo", "nombre", "apellidos")


class ProductoProveedorInline(admin.TabularInline):
    model = ProductoProveedor
    extra = 1


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("codigo", "descripcion", "precio", "existencias")
    search_fields = ("codigo", "descripcion")
    inlines = [ProductoProveedorInline]


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ("id_compra", "cliente", "producto", "fecha")
    list_filter = ("fecha",)
    search_fields = ("cliente__nombre", "producto__descripcion")
