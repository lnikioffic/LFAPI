from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

DB_PATH = BASE_DIR / 'db.sqlite3'

class Settings(BaseSettings):
    db_url: str = f'sqlite+aiosqlite:///{DB_PATH}'


settings = Settings()