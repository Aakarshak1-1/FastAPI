import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DB: str = os.getenv("DB", "")
settings = Settings()
