from django.urls import path
from . import views

urlpatterns = [
    path("", views.proyecto_list, name="gp_proyecto_list"),
    path("nuevo/", views.proyecto_create, name="gp_proyecto_create"),
    path("<str:codigo>/editar/", views.proyecto_update, name="gp_proyecto_update"),
    path("<str:codigo>/eliminar/", views.proyecto_delete, name="gp_proyecto_delete"),
]
