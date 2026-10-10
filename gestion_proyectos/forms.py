from django import forms
from .models import Proyecto


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ["codigo", "descripcion", "cuantia", "fecha_inicio", "fecha_fin", "cliente"]
        widgets = {
            "fecha_inicio": forms.DateInput(attrs={"type": "date"}),
            "fecha_fin": forms.DateInput(attrs={"type": "date"}),
        }
