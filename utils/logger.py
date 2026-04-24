import logging
import os
from config.settings import Settings

def setup_logger():

    level = logging.DEBUG if Settings.ENV == "dev" else logging.INFO

    if not os.path.exists("logs"):
        os.makedirs("logs")

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler("logs/etl.log"),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger()