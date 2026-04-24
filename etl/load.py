from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from config.settings import Settings
from utils.logger import setup_logger

#import enviromental variables
load_dotenv()

#instance the logger variable
logger = setup_logger()

def load_to_db(df):
    """
    Carga DataFrame en PostgreSQL
    """
    try:

        DB_URL = os.getenv(Settings.DB_URL)

        engine = create_engine(DB_URL, echo=False, future=True)

        df.to_sql(
            name='posts_clean',
            con=engine,
            if_exists='append',  # ⚠️ no uses replace aquí
            index=False
        )
    except Exception as e:
        logger.error(f"Error en pipeline: {e}")
        raise