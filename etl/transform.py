import pandas as pd

def transform_posts(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia y transforma datos de la API.
    """

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

    return df
