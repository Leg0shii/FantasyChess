from tables.base_table import Base
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str]
    password: Mapped[str]
