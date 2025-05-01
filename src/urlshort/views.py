from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .models import Urls
from .schemas import URLCreate, URLResponse
from .dependencies import SessionDep
from .service import generate_short_code
from src.database import get_session

urlshort_router = APIRouter()


@urlshort_router.post("/", response_model=URLResponse, status_code=status.HTTP_201_CREATED)
async def create_short_url(url_data: URLCreate, db: SessionDep):
    # Генерация уникального короткого кода
    while True:
        short_code = generate_short_code()
        result = await db.execute(select(Urls).where(Urls.short_url == short_code))
        existing = result.scalar_one_or_none()
        if not existing:
            break

    new_url = Urls(
        original_url=str(url_data.original_url),
        short_url=short_code
    )

    db.add(new_url)
    await db.commit()
    await db.refresh(new_url)

    return {
        "original_url": new_url.original_url,
        "short_url": new_url.short_url
    }


@urlshort_router.get("/{short_url}")
async def redirect_to_original(short_url: str, db: SessionDep):
    result = await db.execute(
        select(Urls).where(Urls.short_url == short_url)
    )
    url_entry = result.scalar_one_or_none()

    if url_entry is None:
        raise HTTPException(status_code=404, detail="Short URL not found")

    return RedirectResponse(url=url_entry.original_url, status_code=307)


