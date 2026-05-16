from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Chama Arbitrator"
    VERTEX_AI_PROJECT: str = ""
    VERTEX_AI_LOCATION: str = "us-central1"
    
    # LLM Hyperparameters
    TEMPERATURE: float = 0.0
    MAX_TOKENS: int = 1024
    
    # Cache Settings
    SEMANTIC_CACHE_THRESHOLD: float = 0.95
    
    class Config:
        env_file = ".env"

settings = Settings()
