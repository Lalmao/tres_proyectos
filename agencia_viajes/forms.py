from django import forms
from .models import Viaje


class ViajeForm(forms.ModelForm):
    class Meta:
        model = Viaje
        fields = ["codigo", "num_plazas", "fecha", "viajero", "origen", "destino"]
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"}),
        }
