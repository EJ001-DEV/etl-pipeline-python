import pandas as pd
from utils.logger import setup_logger

logger = setup_logger()

def transform_posts(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia y transforma datos de la API.
    """
    try:

        # eliminar duplicados
        df = df.drop_duplicates()

        # eliminar registros sin título
        df = df.dropna(subset=['title'])

        # renombrar columnas (clave)
        df = df.rename(columns={
            'userId': 'user_id',
            'id': 'id'
        })

        # crear nueva columna
        df['title_length'] = df['title'].apply(len)

        # filtro lógico
        df = df[df['title_length'] > 10]
        
    except Exception as e:
        logger.error(f"Error en pipeline: {e}")
        raise

    return df
