# Taller U3: Automatización de BD con Python, Faker y Git

Proyecto de la asignatura Bases de Datos para Ciencia de Datos (Universidad de Antioquia).
Autor: [Manuel Araujo Cardenas Colmenares]

## Descripción

Script en Python que se conecta a una base de datos MySQL local con **SQLAlchemy**, crea automáticamente la tabla `personas_manuel`  y la puebla con **100.000 registros** de datos falsos generados con **Faker**. La inserción se hace por lotes de 5.000 registros para mayor velocidad.

## Estructura de la tabla `personas_manuel`

| Columna | Tipo | Descripción |
|---|---|---|
| id | INTEGER (PK, autoincremental) | Identificador único |
| nombre | VARCHAR(100) | Nombre |
| apellido | VARCHAR(100) | Apellido |
| correo | VARCHAR(150) | Correo electrónico |
| telefono | VARCHAR(50) | Teléfono |
| fecha_nacimiento | DATE | Fecha de nacimiento |
| ciudad | VARCHAR(100) | Ciudad |
| direccion | VARCHAR(255) | Dirección |
| empresa | VARCHAR(150) | Empresa |
| profesion | VARCHAR(150) | Profesión |

## Requisitos

- Python 3.10 o superior
- MySQL en ejecución en el equipo local
- Git

## Instalación

1. Clonar el repositorio:

```
   git clone https://github.com/macardenascolmena/taller-u3-faker-mysql.git
   cd taller-u3-faker-mysql
```

2. Crear y activar el entorno virtual (Windows PowerShell):

```
   python -m venv .venv
   .venv\Scripts\Activate.ps1
```

3. Instalar las dependencias:

```
   pip install -r requirements.txt
```

4. Crear la base de datos en MySQL:

```sql
   CREATE DATABASE taller_u3;
```

5. Copiar la plantilla de variables de entorno y completar con tus datos reales:

```
   copy .env.example .env
```

   Editar `.env` con tu usuario, contraseña, host, puerto y nombre de la base de datos.

## Ejecución

```
python main.py
```

El script crea la tabla si no existe, la vacía e inserta 100.000 registros, mostrando el progreso en consola.

## Verificación

```sql
SELECT COUNT(*) FROM taller_u3.personas_manuel;
```

Resultado esperado: `100000`.

## Tecnologías

- Python
- SQLAlchemy
- PyMySQL
- Faker
- python-dotenv
- MySQL