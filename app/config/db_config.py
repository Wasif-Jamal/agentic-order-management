from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config.env_config import settings


class DatabaseConfig:
    def __init__(self):

        self.engine = create_engine(
            settings.DATABASE_URL, connect_args={"check_same_thread": False}
        )

        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

        self.Base = declarative_base()


db_config = DatabaseConfig()
