# ETL Project - API to PostgreSQL

## Descripción
Pipeline ETL que extrae datos desde una API pública, los transforma, valida y los carga en PostgreSQL usando SQLAlchemy con control de idempotencia.

## Tecnologías
- Python
- Pandas
- SQLAlchemy
- PostgreSQL

## Características
- Extracción desde API
- Transformación de datos
- Validación
- Carga con UPSERT (ON CONFLICT)
- Idempotencia

## Ejecución

```bash
python main.py