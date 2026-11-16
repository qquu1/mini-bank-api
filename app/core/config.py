from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Mini Bank API"
    API_V1_STR: str = "/api/v1"

    
    DATABASE_URL: str = "postgresql://postgres:1234aS@localhost:5432/mini_bank_db"
    
    SECRET_KEY: str = "super_secret_key_for_bank_12345"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env" 

settings = Settings()