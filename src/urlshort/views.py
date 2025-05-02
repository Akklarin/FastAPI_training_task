"""API endpoints for URL shortening and redirection.

This module defines the routes for creating short URLs and redirecting
from short codes to the original URLs.
"""

from fastapi import APIRouter, status, HTTPException
from fastapi.responses import RedirectResponse
from .schemas import URLCreate, URLResponse
from .dependencies import SessionDep
from .utils import generate_short_code
from .crud import get_url_by_short_code, create_url

urlshort_router = APIRouter()


@urlshort_router.post(
    "/",
    response_model=URLResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["URL Shortener"]
)
async def create_short_url(url_data: URLCreate, db: SessionDep):
    """
    Create a new short URL.

    Generates a unique short code and saves the original URL in the database.
    Returns the shortened URL.
    """
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
    """
    Redirect to the original URL using the provided short code.

    Raises a 404 error if the short code is not found.
    """
    url_entry = await get_url_by_short_code(db, short_url)

    if url_entry is None:
        raise HTTPException(status_code=404, detail="Short URL not found")

    return RedirectResponse(url=url_entry.original_url, status_code=307)
