from db.connection import engine
from db.models import Base
from sqlalchemy.exc import SQLAlchemyError

def init_db():
    try:
        print("Inicializando base de datos...")

        Base.metadata.create_all(engine)

        print("Tablas creadas correctamente")

    except SQLAlchemyError as e:
        print(f"Error al crear tablas: {e}")
        raise

if __name__ == "__main__":
    init_db()