# ETL Pipeline - API to PostgreSQL

## Inicialización completa BD

```bash
python db/create_database.py
python -m db.init_db
python main.py

## Descripción
Pipeline ETL que extrae datos desde una API, los transforma, valida y los carga en PostgreSQL con control de idempotencia.

## Arquitectura
- Extract: API REST
- Transform: limpieza y reglas de negocio con Pandas
- Load: PostgreSQL usando SQLAlchemy ORM
- Control: UPSERT con ON CONFLICT (idempotencia)
- Logging y manejo de errores

## Tecnologías
- Python
- Pandas
- SQLAlchemy
- PostgreSQL

## Ejecución
```bash
python main.py