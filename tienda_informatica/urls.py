from django.urls import path
from . import views

urlpatterns = [
    path("", views.producto_list, name="ti_producto_list"),
    path("nuevo/", views.producto_create, name="ti_producto_create"),
    path("<str:codigo>/editar/", views.producto_update, name="ti_producto_update"),
    path("<str:codigo>/eliminar/", views.producto_delete, name="ti_producto_delete"),
]
