# ETL Pipeline - API to PostgreSQL


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

## Ejecución:

## Ambiente Dev
```bash
python main.py

## Ambiente Prod
set APP_ENV=prod
python main.py



