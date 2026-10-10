from django.db import models


class Viajero(models.Model):
    dni = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    class Meta:
        db_table = "AV_VIAJERO"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.dni} - {self.nombre}"


class Lugar(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    otros_datos = models.CharField(max_length=200, blank=True)

    class Meta:
        db_table = "AV_LUGAR"
        ordering = ["codigo"]

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Viaje(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    num_plazas = models.IntegerField()
    fecha = models.DateField()
    viajero = models.ForeignKey(Viajero, on_delete=models.CASCADE, db_column="dni_viajero", related_name="viajes")
    origen = models.ForeignKey(Lugar, on_delete=models.PROTECT, db_column="cod_origen", related_name="viajes_origen")
    destino = models.ForeignKey(Lugar, on_delete=models.PROTECT, db_column="cod_destino", related_name="viajes_destino")

    class Meta:
        db_table = "AV_VIAJE"
        ordering = ["codigo"]

    def __str__(self):
        return f"{self.codigo}: {self.origen_id} -> {self.destino_id}"
