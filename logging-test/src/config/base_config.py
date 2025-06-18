import os
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# ENV 값에 따라 로드할 .env 파일 결정
env = os.getenv("ENV", "dev").lower()

env_file_map = {
    "dev": ".env.development",
    "prod": ".env.production",
}

env_file = env_file_map.get(env, ".env.development")
logger.info("env_file=", env_file)
load_dotenv(dotenv_path=env_file)

class Config:
    APP_ENV = os.getenv("APP_ENV", env)
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
    SECRET_KEY = os.getenv("SECRET_KEY", "")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = int(os.getenv("DB_PORT", 5432))
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
