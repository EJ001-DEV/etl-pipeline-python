from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

def load_to_db(df):
    """
    Carga DataFrame en PostgreSQL
    """

    DB_URL = os.getenv("DB_URL")

    engine = create_engine(DB_URL, echo=False, future=True)

    #engine = create_engine(
    #    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    #)

    df.to_sql(
        name='posts_clean',
        con=engine,
        if_exists='append',  # ⚠️ no uses replace aquí
        index=False
    )