from django.contrib import admin
from .models import Viajero, Lugar, Viaje


@admin.register(Viajero)
class ViajeroAdmin(admin.ModelAdmin):
    list_display = ("dni", "nombre", "telefono", "direccion")
    search_fields = ("dni", "nombre")


@admin.register(Lugar)
class LugarAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre", "otros_datos")
    search_fields = ("codigo", "nombre")


@admin.register(Viaje)
class ViajeAdmin(admin.ModelAdmin):
    list_display = ("codigo", "viajero", "origen", "destino", "num_plazas", "fecha")
    list_filter = ("origen", "destino")
    search_fields = ("codigo",)
