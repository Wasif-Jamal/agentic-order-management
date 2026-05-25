from dotenv import load_dotenv
import os


class Settings:

    def __init__(self):
        load_dotenv()

        self.GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
        self.DATABASE_URL = os.getenv("DATABASE_URL")


settings = Settings()