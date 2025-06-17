from pydantic import Json
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str
    DEBUG: bool
    DATABASE:Json[dict]

    class Config:
        env_file = ".env"  # Specify the path to your .env file
        env_file_encoding = "utf-8"