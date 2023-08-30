from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs

from backend.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta
