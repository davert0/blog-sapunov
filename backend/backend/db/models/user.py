from __future__ import annotations
import datetime
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String

from backend.db.base import Base


class User(Base):

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(
        String(length=200), unique=True, nullable=False
    )
    email: Mapped[str] = mapped_column(String(length=200), unique=True, nullable=False)
    password: Mapped[str]
    disabled: Mapped[bool]
    is_admin: Mapped[bool]
    created_date: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r})"
