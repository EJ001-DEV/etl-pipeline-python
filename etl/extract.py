import requests
import pandas as pd

def extract_from_api(url: str) -> pd.DataFrame:
    """
    Hace una petición GET a una API y convierte el JSON en DataFrame.
    """

    response = requests.get(url)

    # status_code 200 = OK
    if response.status_code != 200:
        raise Exception(f"Error en API: {response.status_code}")

    data = response.json()

    # convierte lista de dicts → DataFrame
    df = pd.DataFrame(data)

    return df