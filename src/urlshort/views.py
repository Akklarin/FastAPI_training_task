from fastapi import APIRouter, status, HTTPException
from fastapi.responses import RedirectResponse
from .schemas import URLCreate, URLResponse
from .dependencies import SessionDep
from .service import generate_short_code
from .crud import get_url_by_short_code, create_url

urlshort_router = APIRouter()


@urlshort_router.post("/", response_model=URLResponse, status_code=status.HTTP_201_CREATED, tags=["URL Shortener"])
async def create_short_url(url_data: URLCreate, db: SessionDep):
    while True:
        short_code = generate_short_code()
        existing = await get_url_by_short_code(db, short_code)
        if not existing:
            break

    new_url = await create_url(db, str(url_data.original_url), short_code)

    return {
        "short_url": new_url.short_url
    }


@urlshort_router.get("/{short_url}", tags=["URL Shortener"])
async def redirect_to_original(short_url: str, db: SessionDep):
    url_entry = await get_url_by_short_code(db, short_url)

    if url_entry is None:
        raise HTTPException(status_code=404, detail="Short URL not found")

    return RedirectResponse(url=url_entry.original_url, status_code=307)
