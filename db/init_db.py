from db.connection import engine
from db.models import Base

def init_db():
    Base.metadata.create_all(engine)
    print("Tablas creadas correctamente")

if __name__ == "__main__":
    init_db()