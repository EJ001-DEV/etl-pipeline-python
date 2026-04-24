import time
from etl.pipeline import run_pipeline
from config.settings import Settings
from utils.logger import setup_logger
from db.init_db import init_db
from db.create_database import create_database

logger = setup_logger()

if Settings.ENV == "dev":
    intervalos = 5
else:
    intervalos = 60

if __name__ == "__main__":
    print(f"ENV: {Settings.ENV}")
    print(f"DB_URL: {Settings.DB_URL}")    
    create_database() 
    init_db()
    nContador = 0
    while True:  
        nContador += 1   
        logger.info(f"Runtime # {nContador}")
        run_pipeline()
        time.sleep(intervalos)