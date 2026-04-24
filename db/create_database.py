import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

def create_database():
    db_url = os.getenv("DB_URL")

    # 👉 separar la URL para quitar el nombre de la BD
    base_url = db_url.rsplit("/", 1)[0]
    db_name = db_url.rsplit("/", 1)[1]

    # 👉 conectarse a la BD default (postgres)
    admin_url = f"{base_url}/postgres"

    engine = create_engine(admin_url, isolation_level="AUTOCOMMIT")

    try:
        with engine.connect() as conn:
            conn.execute(text(f"CREATE DATABASE {db_name}"))
            print(f"Base de datos '{db_name}' creada correctamente")

    except Exception as e:
        print(f"Puede que ya exista o error: {e}")