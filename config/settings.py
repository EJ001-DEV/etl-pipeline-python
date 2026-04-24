from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    DB_URL = os.getenv("DB_URL")
    ENV = os.getenv("ENV", "dev")