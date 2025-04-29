from fastapi import APIRouter
from schemas import URLRequest
from dependencies import SessionDep

urlshort_router = APIRouter()


@urlshort_router.post("/", status_code=201)
async def create_short_url(request: URLRequest, session: SessionDep):
    short_id = generate_short_id()
    url_store[short_id] = request.url
    return {"shorten_url_id": short_id}


@urlshort_router.get("/{shorten_url_id:regex(^[a-zA-Z0-9]{6}$)}}", status_code=307)
async def get_original_url(shorten_url_id: str, session: SessionDep):
    original_url = url_store.get(shorten_url_id)
    if not original_url:
        raise HTTPException(status_code=404, detail="Shortened URL not found")
    return {"Location": original_url}