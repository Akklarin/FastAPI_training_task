from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from async_request import router as async_router
import string
import random
import uvicorn

app = FastAPI()

url_store = {}


class URLRequest(BaseModel):
    url: HttpUrl


def generate_short_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


@app.post("/", status_code=201)
async def create_short_url(request: URLRequest):
    short_id = generate_short_id()
    url_store[short_id] = request.url
    return {"shorten_url_id": short_id}


@app.get("/{shorten_url_id:regex(^[a-zA-Z0-9]{6}$)}}", status_code=307)
async def get_original_url(shorten_url_id: str):
    original_url = url_store.get(shorten_url_id)
    if not original_url:
        raise HTTPException(status_code=404, detail="Shortened URL not found")
    return {"Location": original_url}


app.include_router(async_router)


if __name__ == '__main__':
    uvicorn.run('main:app', port=8080, reload=True)