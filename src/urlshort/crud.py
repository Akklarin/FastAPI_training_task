from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Urls


async def get_url_by_short_code(db: AsyncSession, short_code: str) -> Urls | None:
    result = await db.execute(select(Urls).where(Urls.short_url == short_code))
    return result.scalar_one_or_none()


async def create_url(db: AsyncSession, original_url: str, short_code: str) -> Urls:
    new_url = Urls(
        original_url=original_url,
        short_url=short_code
    )
    db.add(new_url)
    await db.commit()
    await db.refresh(new_url)
    return new_url
