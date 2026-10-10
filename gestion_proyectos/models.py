from django.db import models


class Cliente(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    razon_social = models.CharField(max_length=150)
    domicilio = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    class Meta:
        db_table = "GP_CLIENTE"
        ordering = ["codigo"]

    def __str__(self):
        return f"{self.codigo} - {self.razon_social}"


class Colaborador(models.Model):
    nif = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=150)
    domicilio = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    banco = models.CharField(max_length=100)
    numero_cuenta = models.CharField(max_length=30)

    class Meta:
        db_table = "GP_COLABORADOR"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nif} - {self.nombre}"


class TipoPago(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    descripcion = models.CharField(max_length=100)

    class Meta:
        db_table = "GP_TIPO_PAGO"
        ordering = ["codigo"]

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"


class Proyecto(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    descripcion = models.CharField(max_length=200)
    cuantia = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column="codigo_cliente", related_name="proyectos")
    colaboradores = models.ManyToManyField(Colaborador, through="ProyectoColaborador", related_name="proyectos")

    class Meta:
        db_table = "GP_PROYECTO"
        ordering = ["codigo"]

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"


class ProyectoColaborador(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, db_column="codigo_proyecto")
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, db_column="nif_colaborador")

    class Meta:
        db_table = "GP_PROYECTO_COLABORADOR"
        unique_together = ("proyecto", "colaborador")

    def __str__(self):
        return f"{self.proyecto_id} - {self.colaborador_id}"


class Pago(models.Model):
    numero_pago = models.AutoField(primary_key=True)
    concepto = models.CharField(max_length=150)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()
    tipo_pago = models.ForeignKey(TipoPago, on_delete=models.PROTECT, db_column="codigo_tipo_pago", related_name="pagos")
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, db_column="nif_colaborador", related_name="pagos")

    class Meta:
        db_table = "GP_PAGO"
        ordering = ["-fecha_pago"]

    def __str__(self):
        return f"Pago {self.numero_pago} a {self.colaborador_id}"
