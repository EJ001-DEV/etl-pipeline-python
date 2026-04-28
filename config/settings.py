import os
from dotenv import load_dotenv

APP_ENV = os.getenv("APP_ENV", "dev")

print(f"APP_ENV: {APP_ENV}")

env_file = ".env.prod" if APP_ENV == "prod" else ".env"

load_dotenv(env_file)

class Settings:
    ENV = APP_ENV
    DB_URL = os.getenv("DB_URL")