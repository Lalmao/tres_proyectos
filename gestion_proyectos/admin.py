from django.contrib import admin
from .models import Cliente, Colaborador, TipoPago, Proyecto, ProyectoColaborador, Pago


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("codigo", "razon_social", "telefono", "domicilio")
    search_fields = ("codigo", "razon_social")


@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ("nif", "nombre", "telefono", "banco", "numero_cuenta")
    search_fields = ("nif", "nombre")


@admin.register(TipoPago)
class TipoPagoAdmin(admin.ModelAdmin):
    list_display = ("codigo", "descripcion")


class ProyectoColaboradorInline(admin.TabularInline):
    model = ProyectoColaborador
    extra = 1


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ("codigo", "descripcion", "cuantia", "fecha_inicio", "fecha_fin", "cliente")
    list_filter = ("cliente",)
    search_fields = ("codigo", "descripcion")
    inlines = [ProyectoColaboradorInline]


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ("numero_pago", "colaborador", "concepto", "cantidad", "fecha_pago", "tipo_pago")
    list_filter = ("tipo_pago",)
    search_fields = ("concepto",)
