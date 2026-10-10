from django.urls import path
from . import views

urlpatterns = [
    path("", views.viaje_list, name="av_viaje_list"),
    path("nuevo/", views.viaje_create, name="av_viaje_create"),
    path("<str:codigo>/editar/", views.viaje_update, name="av_viaje_update"),
    path("<str:codigo>/eliminar/", views.viaje_delete, name="av_viaje_delete"),
]
