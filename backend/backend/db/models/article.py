from __future__ import annotations
import datetime
from typing import List
from sqlalchemy import Column, Table, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.sqltypes import String

from backend.db.base import Base


article_tag_association = Table(
    "article_tag_association",
    Base.metadata,
    Column("article_id", ForeignKey("article.id"), primary_key=True),
    Column("tag_id", ForeignKey("tag.id"), primary_key=True),
)


class Article(Base):

    __tablename__ = "article"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(length=200))
    text: Mapped[str]
    tags: Mapped[List[Tag]] = relationship(
        "Tag", secondary=article_tag_association, back_populates="articles"
    )
    created_date: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    def __repr__(self) -> str:
        return f"Aricle(id={self.id!r}, name={self.name!r})"


class Tag(Base):

    __tablename__ = "tag"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(length=200))
    articles: Mapped[List[Article]] = relationship(
        secondary=article_tag_association, back_populates="tags"
    )

    def __repr__(self) -> str:
        return f"Tag(id={self.id!r}, name={self.name!r})"
