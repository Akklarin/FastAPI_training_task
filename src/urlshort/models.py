"""SQLAlchemy models for the URL Shortener project."""

from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class Urls(Base):
    __tablename__ = 'urls'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    short_url: Mapped[str] = mapped_column(unique=True)
    original_url: Mapped[str] = mapped_column(nullable=False)
