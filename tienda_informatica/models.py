from django.db import models


class Cliente(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    class Meta:
        db_table = "TI_CLIENTE"
        ordering = ["codigo"]

    def __str__(self):
        return f"{self.codigo} - {self.nombre} {self.apellidos}"


class Proveedor(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    provincia = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    class Meta:
        db_table = "TI_PROVEEDOR"
        ordering = ["codigo"]

    def __str__(self):
        return f"{self.codigo} - {self.nombre} {self.apellidos}"


class Producto(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    descripcion = models.CharField(max_length=150)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    existencias = models.IntegerField(default=0)
    proveedores = models.ManyToManyField(Proveedor, through="ProductoProveedor", related_name="productos")

    class Meta:
        db_table = "TI_PRODUCTO"
        ordering = ["codigo"]

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"


class ProductoProveedor(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column="codigo_producto")
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, db_column="codigo_proveedor")

    class Meta:
        db_table = "TI_PRODUCTO_PROVEEDOR"
        unique_together = ("producto", "proveedor")

    def __str__(self):
        return f"{self.producto_id} - {self.proveedor_id}"


class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column="codigo_producto", related_name="compras")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column="codigo_cliente", related_name="compras")
    fecha = models.DateField()

    class Meta:
        db_table = "TI_COMPRA"
        ordering = ["-fecha"]

    def __str__(self):
        return f"Compra {self.id_compra} - {self.cliente_id}"
