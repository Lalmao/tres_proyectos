import os
import django
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tres_proyectos.settings")
django.setup()

from gestion_proyectos.models import Cliente as GPCliente, Colaborador, TipoPago, Proyecto, ProyectoColaborador, Pago
from tienda_informatica.models import Cliente as TICliente, Proveedor, Producto, ProductoProveedor, Compra
from agencia_viajes.models import Viajero, Lugar, Viaje

# ---------------- Problema 1: Gestion de Proyectos ----------------
clientes1 = [
    ("CLI001", "Constructora Halcón S.A. de C.V.", "Av. Vallarta 1200, GDL", "3331234567"),
    ("CLI002", "Grupo Industrial Tapatío", "Calz. Independencia 450", "3332345678"),
    ("CLI003", "Tecnologías del Pacífico S.A.", "Av. Patria 2300", "3333456789"),
    ("CLI004", "Comercializadora Del Valle", "Av. México 980", "3334567890"),
    ("CLI005", "Distribuidora Jalisco", "Periférico Norte 500", "3335678901"),
    ("CLI006", "Farmacéutica Occidente", "Av. Américas 1500", "3336789012"),
    ("CLI007", "Restaurantes El Fogón", "Av. Chapultepec 320", "3337890123"),
    ("CLI008", "Textiles Guadalajara", "Calz. Lázaro Cárdenas 2100", "3338901234"),
    ("CLI009", "Automotriz Jalisco", "Av. Vallarta 3500", "3339012345"),
    ("CLI010", "Consultores Asociados GDL", "Av. Hidalgo 800", "3330123456"),
]
for c in clientes1:
    GPCliente.objects.update_or_create(codigo=c[0], defaults={"razon_social": c[1], "domicilio": c[2], "telefono": c[3]})

proyectos1 = [
    ("PRY001", "Sistema de inventarios", 150000.00, "2026-01-10", "2026-04-15", "CLI001"),
    ("PRY002", "Sitio web corporativo", 45000.00, "2026-02-01", "2026-03-01", "CLI002"),
    ("PRY003", "App móvil de pedidos", 210000.00, "2026-01-20", None, "CLI007"),
    ("PRY004", "Migración de servidores a la nube", 320000.00, "2026-03-05", None, "CLI003"),
    ("PRY005", "Sistema de nómina", 98000.00, "2026-02-15", "2026-05-15", "CLI008"),
    ("PRY006", "Portal de clientes", 60000.00, "2026-01-05", "2026-02-20", "CLI006"),
    ("PRY007", "Dashboard de ventas", 72000.00, "2026-03-01", None, "CLI005"),
    ("PRY008", "Integración con proveedores", 55000.00, "2026-02-10", "2026-04-01", "CLI004"),
    ("PRY009", "App de rastreo de flotilla", 180000.00, "2026-01-25", None, "CLI009"),
    ("PRY010", "Sistema de reservaciones", 40000.00, "2026-03-10", "2026-04-10", "CLI001"),
]
for p in proyectos1:
    Proyecto.objects.update_or_create(codigo=p[0], defaults={
        "descripcion": p[1], "cuantia": p[2], "fecha_inicio": p[3], "fecha_fin": p[4],
        "cliente_id": p[5],
    })

colaboradores1 = [
    ("GAHM900315KL2", "Marco Antonio García Herrera", "Calle 8 de Julio 120", "3311001001", "BBVA", "0123456789"),
    ("LOPE850722MN5", "Elena López Pérez", "Av. Revolución 450", "3311002002", "Santander", "0234567890"),
    ("RUSC920108PQ3", "Carlos Ruiz Sánchez", "Calle Morelos 230", "3311003003", "Banorte", "0345678901"),
    ("MEDA880930RT9", "Andrea Medina Díaz", "Av. Juárez 88", "3311004004", "BBVA", "0456789012"),
    ("TOGJ950214UV1", "Jorge Torres Gómez", "Calle Hidalgo 15", "3311005005", "HSBC", "0567890123"),
    ("VACL870619WX7", "Laura Vargas Castillo", "Av. Alcalde 900", "3311006006", "Santander", "0678901234"),
    ("NURD910503YZ4", "Daniel Núñez Ramírez", "Calle 5 de Mayo 60", "3311007007", "Banorte", "0789012345"),
    ("ORFS930827AB6", "Sofía Ortiz Flores", "Av. Niños Héroes 320", "3311008008", "BBVA", "0890123456"),
    ("DEMR840111CD8", "Ricardo Delgado Mendoza", "Calle Pedro Moreno 44", "3311009009", "HSBC", "0901234567"),
    ("SAJP960725EF2", "Patricia Salas Jiménez", "Av. Américas 210", "3311010010", "Santander", "0012345678"),
]
for col in colaboradores1:
    Colaborador.objects.update_or_create(nif=col[0], defaults={
        "nombre": col[1], "domicilio": col[2], "telefono": col[3], "banco": col[4], "numero_cuenta": col[5],
    })

asignaciones1 = [
    ("PRY001", "GAHM900315KL2"), ("PRY001", "LOPE850722MN5"), ("PRY002", "RUSC920108PQ3"),
    ("PRY003", "MEDA880930RT9"), ("PRY003", "TOGJ950214UV1"), ("PRY004", "VACL870619WX7"),
    ("PRY005", "NURD910503YZ4"), ("PRY006", "ORFS930827AB6"), ("PRY007", "DEMR840111CD8"),
    ("PRY008", "SAJP960725EF2"), ("PRY009", "GAHM900315KL2"), ("PRY010", "RUSC920108PQ3"),
]
for pc in asignaciones1:
    ProyectoColaborador.objects.update_or_create(proyecto_id=pc[0], colaborador_id=pc[1])

tipos_pago1 = [("TP01", "Transferencia bancaria"), ("TP02", "Depósito"), ("TP03", "Cheque")]
for tp in tipos_pago1:
    TipoPago.objects.update_or_create(codigo=tp[0], defaults={"descripcion": tp[1]})

pagos1 = [
    ("Pago parcial proyecto", 15000, "2026-02-01", "TP01", "GAHM900315KL2"),
    ("Pago parcial proyecto", 12000, "2026-02-05", "TP02", "LOPE850722MN5"),
    ("Pago parcial proyecto", 18000, "2026-02-10", "TP01", "RUSC920108PQ3"),
    ("Pago parcial proyecto", 9000, "2026-02-12", "TP03", "MEDA880930RT9"),
    ("Pago parcial proyecto", 20000, "2026-02-15", "TP01", "TOGJ950214UV1"),
    ("Pago parcial proyecto", 11000, "2026-02-18", "TP02", "NURD910503YZ4"),
    ("Pago parcial proyecto", 13500, "2026-02-20", "TP01", "ORFS930827AB6"),
    ("Pago parcial proyecto", 16000, "2026-02-22", "TP03", "RUSC920108PQ3"),
    ("Pago parcial proyecto", 10000, "2026-02-25", "TP02", "SAJP960725EF2"),
    ("Pago parcial proyecto", 14500, "2026-02-28", "TP01", "DEMR840111CD8"),
    ("Pago parcial proyecto", 17000, "2026-03-01", "TP01", "VACL870619WX7"),
    ("Pago parcial proyecto", 15500, "2026-03-03", "TP02", "GAHM900315KL2"),
]
for pg in pagos1:
    Pago.objects.get_or_create(concepto=pg[0], cantidad=pg[1], fecha_pago=pg[2], tipo_pago_id=pg[3], colaborador_id=pg[4])

print("P1 OK:", GPCliente.objects.count(), Proyecto.objects.count(), Colaborador.objects.count(), Pago.objects.count())

# ---------------- Problema 2: Tienda informatica ----------------
clientes2 = [
    ("C001", "Marisol", "Hernández Luna", "Av. Patria 100", "3321110001"),
    ("C002", "Eduardo", "Campos Ríos", "Calle Reforma 220", "3321110002"),
    ("C003", "Fernanda", "Osorio Villegas", "Av. López Mateos 800", "3321110003"),
    ("C004", "Iván", "Beltrán Soto", "Calle Juárez 15", "3321110004"),
    ("C005", "Daniela", "Paredes Núñez", "Av. Vallarta 2200", "3321110005"),
    ("C006", "Julio César", "Moreno", "Calle Independencia 50", "3321110006"),
    ("C007", "Brenda", "Aguilar Ponce", "Av. Américas 700", "3321110007"),
    ("C008", "Raúl", "Figueroa Camacho", "Calle Morelos 90", "3321110008"),
    ("C009", "Ximena", "Cortés Reyes", "Av. Revolución 330", "3321110009"),
    ("C010", "Héctor", "Lozano Vega", "Calle Hidalgo 44", "3321110010"),
]
for c in clientes2:
    TICliente.objects.update_or_create(codigo=c[0], defaults={"nombre": c[1], "apellidos": c[2], "direccion": c[3], "telefono": c[4]})

proveedores2 = [
    ("PV001", "Tecno", "Distribuciones S.A.", "Av. Mariano Otero 500", "Jalisco", "3341110001"),
    ("PV002", "Silicon", "Importadora de GDL", "Av. Lázaro Cárdenas 1500", "Jalisco", "3341110002"),
    ("PV003", "CompuPartes", "de Occidente", "Calle 8 de Julio 900", "Jalisco", "3341110003"),
    ("PV004", "Grupo", "Hardware MX", "Av. Américas 1800", "CDMX", "3341110004"),
    ("PV005", "Soluciones", "Digitales del Bajío", "Av. Constituyentes 300", "Guanajuato", "3341110005"),
    ("PV006", "Mayoreo", "Electrónico GDL", "Periférico Sur 2200", "Jalisco", "3341110006"),
    ("PV007", "Componentes", "Jalisco S.A.", "Av. Vallarta 4500", "Jalisco", "3341110007"),
    ("PV008", "RedTech", "Proveedores", "Calle Pedro Moreno 300", "Jalisco", "3341110008"),
    ("PV009", "PC", "Wholesale MX", "Av. Patria 3000", "Jalisco", "3341110009"),
    ("PV010", "InfoPartes", "Nacional", "Av. 16 de Septiembre 100", "CDMX", "3341110010"),
]
for p in proveedores2:
    Proveedor.objects.update_or_create(codigo=p[0], defaults={"nombre": p[1], "apellidos": p[2], "direccion": p[3], "provincia": p[4], "telefono": p[5]})

productos2 = [
    ("P001", "Laptop Dell Inspiron 15", 11499.00, 10),
    ("P002", "Laptop HP Pavilion", 15999.00, 8),
    ("P003", "Monitor LG 24 pulgadas", 2899.00, 20),
    ("P004", "Teclado mecánico Logitech", 1299.00, 30),
    ("P005", "Mouse inalámbrico", 249.00, 50),
    ("P006", "Disco SSD 1TB", 1199.00, 25),
    ("P007", "Cable HDMI 2m", 159.00, 60),
    ("P008", "Impresora Epson L3250", 3999.00, 12),
    ("P009", "Router TP-Link AX1800", 1399.00, 18),
    ("P010", "Webcam Logitech C920", 1149.00, 22),
]
for p in productos2:
    Producto.objects.update_or_create(codigo=p[0], defaults={"descripcion": p[1], "precio": p[2], "existencias": p[3]})

pp2 = [("P001", "PV001"), ("P001", "PV002"), ("P002", "PV001"), ("P002", "PV004"), ("P003", "PV002"),
       ("P004", "PV004"), ("P004", "PV006"), ("P005", "PV003"), ("P005", "PV006"), ("P006", "PV002"),
       ("P006", "PV005"), ("P007", "PV005"), ("P007", "PV007"), ("P008", "PV008"), ("P009", "PV006"),
       ("P009", "PV010"), ("P010", "PV001"), ("P010", "PV009")]
for pr in pp2:
    ProductoProveedor.objects.update_or_create(producto_id=pr[0], proveedor_id=pr[1])

compras2 = [
    ("C001", "P001", "2026-01-05"), ("C002", "P003", "2026-01-08"), ("C003", "P002", "2026-01-10"),
    ("C004", "P005", "2026-01-12"), ("C005", "P006", "2026-01-15"), ("C001", "P008", "2026-01-18"),
    ("C006", "P004", "2026-01-20"), ("C007", "P010", "2026-01-22"), ("C008", "P007", "2026-01-25"),
    ("C009", "P009", "2026-01-28"),
]
for cp in compras2:
    Compra.objects.get_or_create(cliente_id=cp[0], producto_id=cp[1], fecha=cp[2])

print("P2 OK:", TICliente.objects.count(), Producto.objects.count(), Proveedor.objects.count(), Compra.objects.count())

# ---------------- Problema 3: Agencia de viajes ----------------
lugares3 = [
    ("LUG001", "Guadalajara"), ("LUG002", "Ciudad de México"), ("LUG003", "Cancún"),
    ("LUG004", "Puerto Vallarta"), ("LUG005", "Monterrey"), ("LUG006", "Los Cabos"),
    ("LUG007", "Oaxaca"), ("LUG008", "Mérida"), ("LUG009", "Madrid"), ("LUG010", "Nueva York"),
]
for l in lugares3:
    Lugar.objects.update_or_create(codigo=l[0], defaults={"nombre": l[1]})

viajeros3 = [
    ("GOHL880413ABC", "Lucía Gómez Hinojosa", "Av. Patria 100", "3341112201"),
    ("PECR910925DEF", "Ricardo Peña Cárdenas", "Calle Juárez 220", "3341112202"),
    ("MARA870630GHI", "Ana María Ramírez", "Av. Vallarta 800", "3341112203"),
    ("SOTJ940218JKL", "Jorge Soto Téllez", "Calle Hidalgo 15", "3341112204"),
    ("CAVL820507MNO", "Lorena Castro Vidal", "Av. México 2200", "3341112205"),
    ("HEND960112PQR", "David Hernández Nava", "Calle Independencia 50", "3341112206"),
    ("OLVS890824STU", "Susana Olvera Salcido", "Av. Américas 700", "3341112207"),
    ("BAMR930305VWX", "Roberto Bautista Mora", "Calle Morelos 90", "3341112208"),
    ("TOGC850919YZA", "Carla Torres González", "Av. Revolución 330", "3341112209"),
    ("FLRP900701BCD", "Pablo Flores Reséndiz", "Calle Hidalgo 44", "3341112210"),
]
for v in viajeros3:
    Viajero.objects.update_or_create(dni=v[0], defaults={"nombre": v[1], "direccion": v[2], "telefono": v[3]})

viajes3 = [
    ("VJ001", 2, "2026-01-05", "GOHL880413ABC", "LUG001", "LUG003"),
    ("VJ002", 1, "2026-01-06", "PECR910925DEF", "LUG001", "LUG002"),
    ("VJ003", 4, "2026-01-08", "MARA870630GHI", "LUG001", "LUG004"),
    ("VJ004", 2, "2026-01-10", "SOTJ940218JKL", "LUG001", "LUG009"),
    ("VJ005", 3, "2026-01-12", "CAVL820507MNO", "LUG002", "LUG007"),
    ("VJ006", 2, "2026-01-14", "HEND960112PQR", "LUG001", "LUG006"),
    ("VJ007", 1, "2026-01-16", "OLVS890824STU", "LUG005", "LUG002"),
    ("VJ008", 2, "2026-01-18", "BAMR930305VWX", "LUG001", "LUG010"),
    ("VJ009", 5, "2026-01-20", "TOGC850919YZA", "LUG003", "LUG001"),
    ("VJ010", 2, "2026-01-22", "FLRP900701BCD", "LUG001", "LUG008"),
    ("VJ011", 2, "2026-01-24", "GOHL880413ABC", "LUG003", "LUG001"),
    ("VJ012", 1, "2026-01-26", "PECR910925DEF", "LUG002", "LUG005"),
]
for v in viajes3:
    Viaje.objects.update_or_create(codigo=v[0], defaults={
        "num_plazas": v[1], "fecha": v[2], "viajero_id": v[3], "origen_id": v[4], "destino_id": v[5],
    })

print("P3 OK:", Lugar.objects.count(), Viajero.objects.count(), Viaje.objects.count())
