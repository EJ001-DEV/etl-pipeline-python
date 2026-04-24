import time
from etl.pipeline import run_pipeline
from config.settings import Settings
from utils.logger import setup_logger

logger = setup_logger()

if Settings.ENV == "dev":
    intervalos = 5
else:
    intervalos = 60

if __name__ == "__main__":
    nContador = 0
    while True:  
        nContador += 1   
        logger.info(f"Runtime # {nContador}")
        run_pipeline()
        time.sleep(intervalos)