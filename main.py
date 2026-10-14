import os
from urllib.parse import quote_plus

from dotenv import load_dotenv
from sqlalchemy import create_engine, text


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


def main():
    engine = get_engine()
    with engine.connect() as conn:
        resultado = conn.execute(text("SELECT VERSION()"))
        print("Conexión exitosa. Versión de MySQL:", resultado.scalar())


if __name__ == "__main__":
    main()