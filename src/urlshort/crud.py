"""CRUD operations for managing URL records in the database."""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Urls


async def get_url_by_short_code(db: AsyncSession, short_code: str) -> Urls | None:
    """
    Retrieve a URL record by its short code.

    Args:
        db (AsyncSession): Database session.
        short_code (str): The short code to look up.

    Returns:
        Urls | None: The URL record if found, otherwise None.
    """
    result = await db.execute(select(Urls).where(Urls.short_url == short_code))
    return result.scalar_one_or_none()


async def create_url(db: AsyncSession, original_url: str, short_code: str) -> Urls:
    """
    Create and persist a new URL record.

    Args:
        db (AsyncSession): Database session.
        original_url (str): The original long URL.
        short_code (str): The generated short code.

    Returns:
        Urls: The newly created URL record.
    """
    new_url = Urls(
        original_url=original_url,
        short_url=short_code
    )
    db.add(new_url)
    await db.commit()
    await db.refresh(new_url)
    return new_url
