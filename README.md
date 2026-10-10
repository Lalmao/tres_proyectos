# Tres proyectos ejemplo — Django + SQLite (un solo framework)

Este proyecto Django contiene los **3 proyectos ejemplo** de la actividad, cada uno como una app independiente dentro del mismo framework (sin mezclar nada nuevo):

| App | Problema | Entidad con ABCD completo (vistas propias) |
|---|---|---|
| `gestion_proyectos` | Problema 1: Gestión de Proyectos | Proyecto |
| `tienda_informatica` | Problema 2: Tienda Informática | Producto |
| `agencia_viajes` | Problema 3: Agencia de Viajes | Viaje |

Todas las demás tablas de cada problema (Cliente, Colaborador, TipoPago, Pago, Proveedor, Compra, Viajero, Lugar, etc.) ya están modeladas y disponibles con Alta/Baja/Cambio/Consulta completos desde el **panel de administración de Django** (`/admin/`) — es Django mismo haciendo el trabajo, no hace falta escribir más pantallas.

Base de datos: **SQLite** (motor SQL, cero configuración, el archivo `db.sqlite3` ya viene con datos de ejemplo cargados).

## Cómo correrlo

```bash
pip install django
cd tres_proyectos
python manage.py runserver
```

Abre `http://127.0.0.1:8000/` — ahí hay un menú con los 3 proyectos y el acceso al panel admin.

**Usuario admin ya creado:**
- Usuario: `admin`
- Contraseña: `admin123`

(entra en `http://127.0.0.1:8000/admin/`)

## Si quieres recargar los datos de ejemplo desde cero

```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser   # o usa el script de abajo
python seed.py
```

El archivo `seed.py` carga 10+ registros por tabla en los 3 proyectos (clientes, proyectos, colaboradores, pagos, productos, proveedores, compras, viajeros, lugares, viajes) — son los mismos datos de ejemplo que ya usaste para validar las consultas de álgebra relacional / SQL de la actividad 3.1, así que todo es consistente entre ambas entregas.

## Qué se probó (de verdad, no solo "compila")

Se corrieron pruebas automáticas con el test client de Django confirmando, para las 3 apps:
- **Alta**: crear un registro nuevo por POST → aparece en la base de datos.
- **Consulta**: aparece correctamente en el listado.
- **Cambio**: editar el registro por POST → el cambio se refleja en la base de datos.
- **Baja**: eliminar el registro por POST → ya no existe en la base de datos.

Y además login exitoso al panel `/admin/`.

## Estructura

```
tres_proyectos/
├── manage.py
├── seed.py                      # carga los datos de ejemplo
├── db.sqlite3                   # base de datos SQLite con datos ya cargados
├── templates/
│   ├── base.html                # navegación entre los 3 proyectos
│   └── home.html
├── tres_proyectos/              # configuración del proyecto Django
│   ├── settings.py
│   └── urls.py
├── gestion_proyectos/           # Problema 1
│   ├── models.py   (Cliente, Proyecto, Colaborador, ProyectoColaborador, TipoPago, Pago)
│   ├── admin.py
│   ├── views.py / forms.py / urls.py
│   └── templates/gestion_proyectos/
├── tienda_informatica/          # Problema 2
│   ├── models.py   (Cliente, Producto, Proveedor, ProductoProveedor, Compra)
│   ├── admin.py
│   ├── views.py / forms.py / urls.py
│   └── templates/tienda_informatica/
└── agencia_viajes/               # Problema 3
    ├── models.py   (Viajero, Lugar, Viaje)
    ├── admin.py
    ├── views.py / forms.py / urls.py
    └── templates/agencia_viajes/
```
