from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    # REDIS_URL: str
    OPENAI_API_KEY: str
    # CELERY_BROKER_URL: str
    # CELERY_RESULT_BACKEND: str

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    class Config:
        env_file = ".env"

settings = Settings()