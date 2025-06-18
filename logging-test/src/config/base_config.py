import os
from pathlib import Path
from dotenv import load_dotenv
from typing import Optional

# 환경 변수 로드
env = os.getenv("ENV", "dev").lower()

# 환경별 .env 파일 매핑
env_file_map = {
    "dev": ".env.development",
    "prod": ".env.production",
}

# .env 파일 로드
env_file = env_file_map.get(env, ".env.development")
load_dotenv(dotenv_path=env_file)

# 애플리케이션 루트 디렉토리
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# class Config:
#     APP_ENV = os.getenv("APP_ENV", env)
#     DEBUG = os.getenv("DEBUG", "false").lower() == "true"
#     SECRET_KEY = os.getenv("SECRET_KEY", "")
#     DB_HOST = os.getenv("DB_HOST", "localhost")
#     DB_PORT = int(os.getenv("DB_PORT", 5432))
#     DB_USER = os.getenv("DB_USER")
#     DB_PASSWORD = os.getenv("DB_PASSWORD")
class Config:
    
    """기본 설정 클래스"""
    # 애플리케이션 설정
    APP_ENV: str = os.getenv("APP_ENV", env)
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "")
    
    # 데이터베이스 설정
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", "5432"))
    DB_USER: str = os.getenv("DB_USER", "")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    
    # 로깅 설정
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "DEBUG" if APP_ENV == "dev" else "INFO")
    LOG_DIR: str = os.getenv("LOG_DIR", str(BASE_DIR / "logs"))
    ENABLE_FILE_LOGGING: bool = os.getenv("ENABLE_FILE_LOGGING", "true").lower() == "true"
    
    @classmethod
    def to_dict(cls) -> dict:
        """설정을 딕셔너리로 변환 (로깅용)"""
        config_dict = {}
        for key in dir(cls):
            if key.isupper() and not key.startswith('_'):
                value = getattr(cls, key)
                # 민감한 정보는 마스킹
                if any(sensitive in key.lower() for sensitive in ['key', 'pass', 'secret']):
                    value = '***MASKED***' if value else None
                config_dict[key] = value
        return config_dict

# 로깅 설정 초기화 (main 모듈에서 import 시점에 설정)
def init_logging():
    """로깅 초기화"""
    from .logging_config import setup_logging
    setup_logging(
        app_env=Config.APP_ENV,
        log_level=Config.LOG_LEVEL,
        log_dir=Config.LOG_DIR
    )

# 모듈 임포트 시 자동으로 로깅 초기화
if os.getenv("SKIP_LOGGING_INIT", "false").lower() != "true":
    init_logging()
