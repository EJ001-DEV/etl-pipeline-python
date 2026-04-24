import os
from dotenv import load_dotenv

ENV = os.getenv("APP_ENV", "dev")

env_file = ".env.prod" if ENV == "prod" else ".env"

load_dotenv(env_file)

class Settings:
    ENV = ENV
    DB_URL = os.getenv("DB_URL")