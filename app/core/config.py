from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Diet Plan API"
    MONGO_URI: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "diet_plan"
    SECRET_KEY: str = "your-secret-key"  # In production, use environment variable
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours

settings = Settings()