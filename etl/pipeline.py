from etl.extract import extract_from_api
from etl.transform import transform_posts
from etl.validate import validate_data
from etl.upsert import upsert_posts
from db.connection import engine
from utils.logger import setup_logger
from config.settings import Settings

logger = setup_logger()

def run_pipeline():

    logger.info(f"Ejecutando en entorno: {Settings.ENV}")

    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        df = extract_from_api(url)

        df = transform_posts(df)

        issues = validate_data(df)

        upsert_posts(df, engine)

        logger.info("Pipeline ejecutado correctamente")

        logger.info(issues)
        #print("Pipeline ejecutado correctamente")
        #print("Issues:", {k: len(v) for k, v in issues.items()})

    except Exception as e:
        logger.error(f"Error en pipeline: {e}")
        raise