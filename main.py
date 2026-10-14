import os
from urllib.parse import quote_plus

from dotenv import load_dotenv
from sqlalchemy import (
    Column,
    Date,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
)

TABLE_NAME = "personas_manuel"


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


def main():
    engine = get_engine()
    metadata = MetaData()
    define_table(metadata)

    # Crea la tabla solo si no existe
    metadata.create_all(engine)
    print(f"Tabla '{TABLE_NAME}' lista.")


if __name__ == "__main__":
    main()