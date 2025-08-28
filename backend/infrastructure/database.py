from contextlib import contextmanager
import os
from typing import Any, Generator

from dotenv import load_dotenv
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session

from tables.base_table import Base
from tables.user import User


load_dotenv()


class DatabaseManager:

    def __init__(self) -> None:
        self.engine = self.initialize_connection()
        self.create_tables()

    def initialize_connection(self) -> Engine:
        user = os.getenv("DATBASE_USER", "postgres")
        password = os.getenv("DATBASE_PASSWORD", "password")
        hostname = os.getenv("DATBASE_HOSTNAME", "localhost")
        database_name = os.getenv("DATBASE_NAME", "postgres")
        port = int(os.getenv("DATBASE_PORT", 5432))

        return create_engine(f"postgresql+psycopg2://{user}:{password}@{hostname}:{port}/{database_name}", echo=True)

    @contextmanager
    def session_scope(self) -> Generator[Session, Any, Any]:
        session = Session(self.engine)
        try:
            yield session
        finally:
            session.commit()

    def create_tables(self) -> None:
        Base.metadata.create_all(bind=self.engine)


if __name__ == "__main__":
    db = DatabaseManager()
