import os
from urllib.parse import quote_plus

from dotenv import load_dotenv
from faker import Faker
from sqlalchemy import (
    Column,
    Date,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
    insert,
    text,
)

TABLE_NAME = "personas_manuel"
TOTAL_REGISTROS = 100_000
TAMANO_LOTE = 5_000


def get_engine():
    """Crea el engine de SQLAlchemy usando las variables del archivo .env"""
    load_dotenv()

    user = os.getenv("DB_USER")
    password = quote_plus(os.getenv("DB_PASSWORD"))
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")

    url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}"
    return create_engine(url)


def define_table(metadata):
    """Define la estructura de la tabla personas_manuel"""
    return Table(
        TABLE_NAME,
        metadata,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("nombre", String(100), nullable=False),
        Column("apellido", String(100), nullable=False),
        Column("correo", String(150)),
        Column("telefono", String(50)),
        Column("fecha_nacimiento", Date),
        Column("ciudad", String(100)),
        Column("direccion", String(255)),
        Column("empresa", String(150)),
        Column("profesion", String(150)),
    )
    

def generar_personas(fake, cantidad):
    """Genera una lista de diccionarios con datos falsos"""
    personas = []
    for _ in range(cantidad):
        personas.append(
            {
                "nombre": fake.first_name(),
                "apellido": fake.last_name(),
                "correo": fake.email(),
                "telefono": fake.phone_number(),
                "fecha_nacimiento": fake.date_of_birth(minimum_age=18, maximum_age=90),
                "ciudad": fake.city(),
                "direccion": fake.address().replace("\n", ", "),
                "empresa": fake.company(),
                "profesion": fake.job(),
            }
        )
    return personas


def main():
    engine = get_engine()
    metadata = MetaData()
    tabla = define_table(metadata)

    # Crea la tabla solo si no existe
    metadata.create_all(engine)
    print(f"Tabla '{TABLE_NAME}' lista.")

    fake = Faker("es_CO")

    # Vacía la tabla para que ejecutar el script varias veces no duplique datos
    with engine.begin() as conn:
        conn.execute(text(f"TRUNCATE TABLE {TABLE_NAME}"))

    insertados = 0
    while insertados < TOTAL_REGISTROS:
        lote = generar_personas(fake, TAMANO_LOTE)
        with engine.begin() as conn:
            conn.execute(insert(tabla), lote)
        insertados += TAMANO_LOTE
        print(f"Insertados {insertados} de {TOTAL_REGISTROS}")

    print("Inserción completada.")


if __name__ == "__main__":
    main()