from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL")


settings = Settings()